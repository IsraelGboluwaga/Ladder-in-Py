from twilio import TwilioRestClient

client = TwilioRestClient()

client.messages.create(from_="(817) 752-1632",
                       to = "(706) 259-2846",
                       body= "This msg was sent with python. No shaking.")

#Save and run =, maybe on terminal.