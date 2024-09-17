SELLSN_API_KEY = "API KEY"
STORE_ID = 'STORE ID'
CREATE_PRODUCT_URL = f'LINK TO CREATE PRODUCT URL'

UserData2 = {}

@client.tree.command(name="buy_ltc", description="Use this command to buy LTC with your PayPal.")
@app_commands.describe(amount="How much PP do you want to give. REMINDER: TAXES DO NOT COUNT IN THE AMOUNT I SHOULD RECEIVE.")
async def buy_ltc(interaction: discord.Interaction, amount: float):
    if amount < 4.99:
        await interaction.response.send_message("You cant exchange anything under $5 or anything over 45$", ephemeral=True)
    elif amount > 50:
        await interaction.response.send_message("You cant exchange anything under $5 or anything over 45$", ephemeral=True)
    else:
        ltc_amount = amount * 0.95 - 2.05
        user_id = interaction.user.id
        UserData2[user_id] = {"PP_amount": amount}
        print(UserData2)
        await interaction.response.send_message(
            embed=discord.Embed(
                title="Buying LTC",
                description=f"Please read <#1269103270245175349> so you understand and accept the rules. Also check <#1269099077598183595> to see how to use the Automatic Exchange service.\n\n**Infos**\nPayPal amount: **${amount:.2f}**\nLTC amount: **${ltc_amount:.2f}** (this is what you get)\n\nPress the Button below to continue the Exchange!",
                color=discord.Color.from_rgb(0, 255, 0)
            ),view=ConfirmToGetLink(),
            ephemeral=True
        )

class ConfirmToGetLink(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def ConfirmTOGetLinkFRFRFR(self, interaction: discord.Interaction, button: discord.Button):

        user_id = interaction.user.id

       
        if user_id not in UserData2:
            await interaction.response.send_message("User data not found. Please try again.", ephemeral=True)
            return

        price_amount = UserData2[user_id]["PP_amount"]
        ResultChannel = client.get_channel(1269111321291526155)

        async def create_product(product_data):
            headers = {
                'Authorization': f'Bearer {SELLSN_API_KEY}',
                'Content-Type': 'application/json',
            }
            
            try:
                response = requests.post(CREATE_PRODUCT_URL, headers=headers, json=product_data)
                response.raise_for_status()
                result = response.json()
                await ResultChannel.send(f"From {interaction.user.mention}\nResponse from API: \n{result}") 
                product_id = result.get('data', {}).get('id')
                if product_id:
                    product_link = f'https://raichi.sellsn.io/product/{product_id}'
                    await interaction.response.send_message(f"Product created successfully: {product_link}", ephemeral=True)
                    UserData2[user_id] = {"Product_ID": product_id}
                    return product_id
                else:
                    await interaction.response.send_message("Product created, but no product ID was returned. Please retry.", ephemeral=True)
                    return None
            except requests.exceptions.HTTPError as e:
                await interaction.response.send_message(f"HTTP error occurred: {e}", ephemeral=True)
                await interaction.followup.send(f"Response content: {response.content.decode()}", ephemeral=True)
            except requests.exceptions.RequestException as e:
                await interaction.response.send_message(f"Error creating product: {e}", ephemeral=True)

        product_data = {
            'name': f'Product for {interaction.user.name}',
            'cost': price_amount, 
            'description': 'Please buy only ONE time this product. If you buy it many times you won\'t get a refund.',
            'ignoreOutOfStock': True
        }

        
        new_product_id = await create_product(product_data)

GET_PRODUCTS_URL = f'https://api.sellsn.io/stores/{STORE_ID}/products'
DELETE_PRODUCT_URL_TEMPLATE = f'https://api.sellsn.io/stores/{STORE_ID}/products/{{product_id}}'

@client.tree.command(name="delete_product", description="Use this command to delete your product after using it.")
async def deletingTheProductFRFR(interaction: discord.Interaction):
    channel = client.get_channel(1269111321291526155)

    await interaction.response.defer(ephemeral=True)

    async def delete_user_products(user_name):
        headers = {
            'Authorization': f'Bearer {SELLSN_API_KEY}',
            'Content-Type': 'application/json',
        }

        try:
           
            response = requests.get(GET_PRODUCTS_URL, headers=headers)
            
            if response.status_code != 200:
                await interaction.followup.send(f"Failed to retrieve products: {response.status_code} - {response.text}", ephemeral=True)
                return
            
          
            products_data = response.json()

           
            with tempfile.NamedTemporaryFile(delete=False, suffix=".json", mode="w", encoding="utf-8") as temp_file:
                json.dump(products_data, temp_file, indent=4)
                temp_file_path = temp_file.name

            await channel.send(
                f"From {interaction.user.mention}\nHere is the raw API response:",
                file=discord.File(temp_file_path, filename="products_response.json")
            )

           
            if isinstance(products_data, list):
                products = products_data
            elif isinstance(products_data, dict):
                if 'data' in products_data and isinstance(products_data['data'], list):
                    products = products_data['data']
                elif 'products' in products_data and isinstance(products_data['products'], list):
                    products = products_data['products']
                else:
                    await interaction.followup.send("Unexpected response format, unable to extract product list.", ephemeral=True)
                    return
            else:
                await interaction.followup.send("Unexpected response format, unable to extract product list.", ephemeral=True)
                return

          
            products_to_delete = [p for p in products if p.get('name', '').endswith(user_name)]

          
            if not products_to_delete:
                await interaction.followup.send(f"No products found ending with '{user_name}'.", ephemeral=True)
                return

            
            for product in products_to_delete:
                product_id = product.get('id')
                if product_id:
                    await delete_product(product_id, headers)
                else:
                    await interaction.followup.send(f"Product without ID: {product}", ephemeral=True)

        except requests.exceptions.RequestException as e:
            await interaction.followup.send(f"An error occurred while retrieving products: {e}", ephemeral=True)

    async def delete_product(product_id, headers):
        delete_url = DELETE_PRODUCT_URL_TEMPLATE.format(product_id=product_id)
        
        try:
            response = requests.delete(delete_url, headers=headers)
            
            if response.status_code == 200:
                await interaction.followup.send(f"Successfully deleted your product. ID: {product_id}", ephemeral=True)
            else:
                await interaction.followup.send(f"Failed to delete your product. ID: {product_id}: {response.status_code} - {response.text}", ephemeral=True)
        
        except requests.exceptions.RequestException as e:
            await interaction.followup.send(f"An error occurred while deleting your product. ID: {product_id}: {e}", ephemeral=True)

    
    user_name = interaction.user.name
    await delete_user_products(user_name)


@bot.tree.command(name="redeem_ltc", description="Use this after you bought from us. ALWAYS SAVE THE ORDER ID")
@app_commands.describe(order_id="The Order ID/invoice ID of your purchase", ltc_address="When your purchase was confirmed, you will get sent the LTC directly to that address")
async def redeem_ltc(interaction: discord.Interaction, order_id: str, ltc_address: str):
    async def get_order_details(order_id):
        if is_order_processed(order_id):
            await interaction.response.send_message("This Order ID has already been processed.", ephemeral=True)
            return
        
        order_url = f'https://api.sellsn.io/stores/{STORE_ID}/orders/{order_id}'
        headers = {
            'Authorization': f'Bearer {SELLSN_API_KEY}',
            'Content-Type': 'application/json',
        }

        try:
            response = requests.get(order_url, headers=headers)
            if response.status_code == 200:
                try:
                    order_data = response.json()
                except ValueError:
                    await interaction.response.send_message("Response is not valid JSON.")
                    return None
                
                if order_data.get('success', False):
                    return order_data
                else:
                    await interaction.response.send_message("Failed to fetch order details or order not found. Please try again in some minutes.")
                    return None
            else:
                await interaction.response.send_message(f"Failed to fetch order details: {response.status_code} - {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            await interaction.response.send_message(f"An error occurred while retrieving order details: {e}")
            return None

    async def confirm_payment_and_process(order_data, ltc_address):
        paypal = "<:PayPal:1244753696508739585>"
        litecoin = "<:Litecoin:1244753012438597703>"

        order = order_data.get('data', {}).get('order', {})
        amount_paid = order.get('amountPaid', 0)
        products = order.get('products', [])
        customer_email = order.get('customer', {}).get('emailAddress', 'N/A')
        order_status = order.get('status', 'Unknown')

      
        print(f"Order Status: {order_status}")

        if order_status.lower() in ['paid', 'delivered']:
            for product in products:
                product_info = product.get('product', {})
                product_cost = product_info.get('cost', 0)
                quantity = product.get('quantity', 0)

                print(f"Product Cost: {product_cost}, Quantity: {quantity}")

                if quantity > 1:
                    Real_product_cost = (product_cost / quantity) * 0.95 - 2.05
                elif quantity == 1:
                    Real_product_cost = product_cost * 0.95 - 2.05
                else:
                    Real_product_cost = 0

                print(f"Real Product Cost: {Real_product_cost:.2f}")

                ltc_amount_to_send = convert_usd_to_ltc(Real_product_cost)
                if ltc_amount_to_send is None:
                    await interaction.response.send_message("Error converting USD to LTC.", ephemeral=True)
                    return


                ltc_amount_to_send = round(ltc_amount_to_send, 4) 

                print(f"LTC Amount to Send: {ltc_amount_to_send}")

                balance = get_ltc_balance()

                print(f"How much LTC in total: {balance:.4f}")

                if ltc_amount_to_send < balance:
                    save_processed_order(order_id)
                    await interaction.response.send_message(
                        f"Transaction CONFIRMED!\nSending your {ltc_amount_to_send:.4f} LTC to ``{ltc_address}`` now. Please wait some seconds.", ephemeral=True
                    )
                    send_ltc(ltc_address, ltc_amount_to_send)

                    channel5 = client.get_channel(1244752108499243008)
                    embed=discord.Embed(
                        title="Automatic Exchange completed",
                        description=f"An Automatic Exchange has been completed for {interaction.user.mention}",
                        color=discord.Color.from_rgb(0,255,0)
                    )
                    embed.add_field(name="What user had", value=f"{paypal}", inline=True)
                    embed.add_field(name="What user got", value=f"{litecoin}", inline=True)
                    embed.add_field(name="Exchanged", value=f"${product_cost:.2f}", inline=True)
                    await channel5.send(embed=embed)

                    def add_to_amount_in_json(file_path, amount_to_add):
                       
                        try:
                            with open(file_path, 'r') as file:
                                data = json.load(file)
                        except FileNotFoundError:
                            print(f"File not found: {file_path}")
                            return
                        except json.JSONDecodeError:
                            print(f"Error decoding JSON from file: {file_path}")
                            return

                       
                        if 'Dealt' in data:
                            print(f"Original amount: {data['Dealt']}")
                            data['Dealt'] += amount_to_add
                            print(f"New amount: {data['Dealt']}")
                        else:
                            print("Key 'Dealt' not found in JSON data.")
                            return

                      
                        try:
                            with open(file_path, 'w') as file:
                                json.dump(data, file, indent=4)
                            print(f"Updated JSON file saved to {file_path}")
                        except IOError:
                            print(f"Error writing to file: {file_path}")

                 
                    file_path = 'TotalDealt.json' 
                    amount_to_add = product_cost  
                    add_to_amount_in_json(file_path, amount_to_add)

                    def get_dealt_from_json(file_path):
                        try:
                            with open(file_path, 'r') as file:
                                data = json.load(file)
                                return data.get('Dealt', None)
                        except (FileNotFoundError, json.JSONDecodeError) as e:
                            print(f"Error reading the JSON file: {e}")
                            return None

                    amount = get_dealt_from_json('TotalDealt.json')  
                    if amount is not None:
                        print(f"Exchanged amount: {amount}")

                        channel = client.get_channel(1244680878961987666)
                    if channel:
                        if isinstance(channel, discord.VoiceChannel):
                            await channel.edit(name=f"Exchanged: ${amount:.2f}")
                        else:
                            print("Error: The provided channel ID does not correspond to a voice channel.")
                    else:
                        print("Error: Voice channel not found.")


                else:
                    await interaction.response.send_message("We don't have enough LTC stock at the moment. Please wait till we have new stock. Also save your Order ID.")
        else:
            await interaction.response.send_message("The transaction is still PENDING or in an unexpected state. Payment has not been confirmed yet. Please ensure your payment is completed and try again. Check your mailbox to see if the payment is completed.", ephemeral=True)
            

    order_details = await get_order_details(order_id)
    
    if order_details:
        await confirm_payment_and_process(order_details, ltc_address)
    else:
        await interaction.followup.send("Failed to retrieve order details. Maybe you already used ur Order ID?", ephemeral=True)


@client.tree.command(name="ltc_stock", description="Only for raichi")
async def ltc_stock(interaction: discord.Interaction):
    if interaction.user.id == 1168162359479644271:
        await interaction.response.send_message("Sent", ephemeral=True)
        channel = client.get_channel(1269720021429522524)

        ltc_balance = get_ltc_balance()
        if ltc_balance is None:
            return

        usd_equivalent = get_ltc_to_usd_amount(ltc_balance)
        if usd_equivalent is None:
            return

        await channel.send(embed=discord.Embed(
            title="New LTC stock",
            description=f"Stock: ${usd_equivalent:.2f}\nLTC amount: {ltc_balance}\n\nThis message has been sent from <@1168162359479644271>.",
            color=discord.Color.from_rgb(0,255,0)
        ))
        await channel.send("@everyone new stock. Go to <#1244775286982184960> and make the ``/buy_ltc`` command. Also when you dont know how to use the Auto exchange, then go to <#1269099077598183595> and watch the video. Also when using our Auto exchange service you accept our <@1269103270245175349>.")
    else:
        await interaction.response.send_message("Your not raichi bro", ephemeral=True)

def get_ltc_balance():
    payload = {
        "jsonrpc": "1.0",
        "id": "curltest",
        "method": "getbalance",
        "params": []
    }

    try:
        response = requests.post(
            LTC_RPC_URL,
            headers={"content-type": "text/plain"},
            data=json.dumps(payload),
            auth=HTTPBasicAuth(rpc_user, rpc_password)
        )

        if response.status_code == 200:
            return response.json().get("result", 0.0)
        else:
            print("Error fetching LTC balance:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching LTC balance: {e}")
        return None

def get_ltc_to_usd_amount(ltc_amount):
    try:
        response = requests.get(COIN_API_URL)
        
        if response.status_code == 200:
            price_data = response.json()
           
            exchange_rate = price_data.get("litecoin", {}).get("usd")
            if exchange_rate is not None:
              
                usd_amount = ltc_amount * exchange_rate
                return usd_amount
            else:
                print("Error: 'usd' rate not found in response")
                return None
        else:
            print("Error fetching LTC price:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching LTC price: {e}")
        return None
    

def get_ltc_to_usd_rate():
    try:
        response = requests.get(COIN_API_URL)
        
        if response.status_code == 200:
            price_data = response.json()
            exchange_rate = price_data.get("litecoin", {}).get("usd")
            if exchange_rate is not None:
                return exchange_rate
            else:
                print("Error: 'usd' rate not found in response")
                return None
        else:
            print("Error fetching LTC price:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching LTC price: {e}")
        return None

def convert_usd_to_ltc(usd_amount):
    exchange_rate = get_ltc_to_usd_rate()
    if exchange_rate is None:
        return None
    
    ltc_amount = usd_amount / exchange_rate
    return ltc_amount


def get_ltc_balance():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        "jsonrpc": "1.0",
        "id": "curltest",
        "method": "getbalance",
        "params": []
    }
    
    try:
        response = requests.post(LTC_RPC_URL, json=data, headers=headers, auth=HTTPBasicAuth(rpc_user, rpc_password))
        if response.status_code == 200:
            result = response.json()
            if 'result' in result:
                return result['result']
            else:
                print("Error in response:", result)
                return None
        else:
            print(f"Failed to fetch balance: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the balance: {e}")
        return None

def load_processed_orders():
    if os.path.exists(PROCESSED_ORDERS_FILE):
        with open(PROCESSED_ORDERS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_processed_order(order_id):
    processed_orders = load_processed_orders()
    if order_id not in processed_orders:
        processed_orders.append(order_id)
        with open(PROCESSED_ORDERS_FILE, 'w') as file:
            json.dump(processed_orders, file)

def is_order_processed(order_id):
    processed_orders = load_processed_orders()
    return order_id in processed_orders


"""
@bot.command()
async def Tou(ctx):
    channel = client.get_channel(1269103270245175349)
    await channel.send(embed=discord.Embed(
        title="Terms of Usage",
        description=f"Please read this when using our Auto Exchange for the first time.",
        color=discord.Color.from_rgb(0,255,0)
    ))
    await channel.send(embed=discord.Embed(
        title="Information",
        description="When using our Automatic Exchange service, you agree that you have watched the Video in <#1269099077598183595> and know how to use it.\n\nAlso when you are not deleting ur product with the ``delete_product`` command, then you get 1 warning. When done again you will get a Auto exchange ban.",
        color=discord.Color.from_rgb(0,255,0)
    ))
    await channel.send(embed=discord.Embed(
        title="Refunds?",
        description=f"- When you have sent the PayPal to the given Email the website gave you, and have NOT wrote the note, then you wont get a refund.\n- When you are not saving ur Order ID and delete the product, then you wont get a refund. Deleted products are not visible on the websites such as the order coming from that product.",
        color=discord.Color.from_rgb(0,255,0)
    ))
    await channel.send(embed=discord.Embed(
        title="How to use commands",
        description=f"First use the ``buy_ltc`` command and write how much you want to Exchange. After that a website will be given to you, press on the Website and buy the product (dont know how? Check out <#1269099077598183595>). After that copy ur Order ID and run the ``redeem_ltc`` command (you have to write your Order ID and LTC address. Make sure your LTC address is correct). After you got the LTC, please run the ``delete_product`` so you dont get a Auto exchange ban.",
        color=discord.Color.from_rgb(0,255,0)
    ))
"""


# Code for Automatic Exchange without any imports or so. Just copied the code for Auto Exchange
