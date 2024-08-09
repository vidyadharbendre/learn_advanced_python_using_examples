import streamlit as st
import pandas as pd
from notifier.send_message import WhatsAppNotifier

def main():
    st.title("WhatsApp Notifier")
    
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])
    
    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)
            st.write("File successfully loaded.")
            st.write(df)
            
            message = st.text_area("Enter the message to send")
            group_name = st.text_input("Enter the WhatsApp group name")
            
            if st.button("Send Message Now"):
                driver_path = '/path/to/chromedriver'
                contacts = df['Phone Number'].tolist()
                notifier = WhatsAppNotifier(driver_path)
                st.write("Please scan the QR code in the opened browser window.")
                notifier._init_driver()  # Open browser and scan QR code
                notifier.wait_for_login()
                if group_name:
                    notifier.send_group_message(group_name, message)
                else:
                    send_messages(driver_path, contacts, message)
                notifier.close()
        except Exception as e:
            st.error(f"Error processing file: {e}")

if __name__ == "__main__":
    main()
