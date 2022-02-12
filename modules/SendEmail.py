import os
import smtplib
from emailList import email_receivers


class SendEmail:
    def __init__(self, item_ID, price, url):

        """
        email address and password are save in os environment
        """
        self.email = os.environ.get("EMAIL_ADDRESS")
        self.password = os.environ.get("EMAIL_PASSWORD")

        self.item = item_ID
        self.price = price
        self.url = url

    def Send(self):

        """Use Gmail Server to send emails. Use the following url to set less secure Gmail access
        https://myaccount.google.com/lesssecureapps"""

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.email, self.password)

            subject = f"{self.item} ${self.price} is back stock!"

            msg = f"Subject: {subject} \n\n {self.url}"

            smtp.sendmail(self.email, email_receivers, msg)
