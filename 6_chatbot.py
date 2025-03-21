import os
os.system('say "Hey I am your scholarlogic chatbot. I am here to help you with your payment related queries. Please select the options from below"')

print( "\n Hello, \n I am a chatbot. I am here to help you with your queries. Please select the options from below.\n")
print("\n 1. Payment Issues \n 2. Profile and Payments \n 3. Money Transfer \n 4. Recharge anbd Bill Payments \n 5. Reward Refer and Earn \n 6. Others")
choice = int(input("Enter the option number: "))
if choice==1:
    print("\n Payment Issues: \n 1. Issues with Failed Payments \n 2. Issues with Pending Payments \n 3. Issues with Successfull Payments \n 4. Issues with payments made to merchants \n 5. Issues with refunds")
    choice1= int(input("Enter the option number: "))
    if choice1==1:
        print ("\n Issues with Failed Payments: \n 1. Why did my UPI Payment Failed \n 2. Why is my money deducted for my failed payment \n 3. Why is my money not refunded yet \n 4. Where can I find the UTR number.")
        input2= int(input("Enter the option number-: "))
        if input2==1:
            print("\n UPI Payment Failed: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input2==2:
            print("\n Money Deducted for Failed Payment: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input2==3:
            print("\n Money not refunded yet: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input2==4:
            print("\n UTR Number: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        else:
            print("\n Invalid Input")
    elif choice1==2:
        print("\n Issues with Pending Payments: \n 1. Why is my payment pending \n 2. How to cancel a pending payment \n 3. How to check the status of a pending payment \n 4. How to make a payment successful")
        input3= int(input("Enter the option number-: "))
        if input3==1:
            print("\n Payment Pending: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input3==2:
            print("\n Cancel a Pending Payment: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input3==3:
            print("\n Check the Status of a Pending Payment: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input3==4:
            print("\n Make a Payment Successful: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        else:
            print("\n Invalid Input")
    elif choice1==3:
        print("\n Issues with Successfull Payments: \n 1. Why is my payment not reflecting in my account \n 2. How to check the status of a successfull payment \n 3. How to get a receipt for a successfull payment \n 4. How to get a refund for a successfull payment")
        input4= int(input("Enter the option number-: "))
        if input4==1:
            print("\n Payment not reflecting in my account: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input4==2:
            print("\n Check the Status of a Successfull Payment: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input4==3:
            print("\n Get a Receipt for a Successfull Payment: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input4==4:
            print("\n Get a Refund for a Successfull Payment: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        else:
            print("\n Invalid Input")
    elif choice1==4:
        print("\n Issues with payments made to merchants: \n 1. Why is my payment to merchant pending \n 2. How to cancel a payment to merchant \n 3. How to check the status of a payment to merchant \n 4. How to make a payment to merchant successful") 
        input5= int(input("Enter the option number-: "))
        if input5==1:
            print("\n Payment to Merchant Pending: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input5==2:
            print("\n Cancel a Payment to Merchant: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input5==3:
            print("\n Check the Status of a Payment to Merchant: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input5==4:
            print("\n Make a Payment to Merchant Successful: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        else:
            print("\n Invalid Input")
    elif choice1==5:
        print("\n Issues with refunds: \n 1. Why is my refund pending \n 2. How to cancel a refund \n 3. How to check the status of a refund \n 4. How to make a refund successful")
        input6= int(input("Enter the option number-: "))
        if input6==1:
            print("\n Refund Pending: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input6==2:
            print("\n Cancel a Refund: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input6==3:
            print("\n Check the Status of a Refund: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        elif input6==4:
            print("\n Make a Refund Successful: \n 1. Check if your bank account is active \n 2. Check if your bank account is linked to your UPI \n 3. Check if your UPI pin is correct \n 4. Check if you have sufficient balance in your account")
        else:
            print("\n Invalid Input")
    else:
        print("\n Invalid Input")
elif choice==2:
    print("\n Profile and Payments: \n 1. How to update my profile \n 2. How to change my password \n 3. How to change my email id \n 4. How to change my phone number")
    choice2= int(input("Enter the option number: "))
    if choice2==1:
        print("\n Update my Profile: \n 1. Go to Profile \n 2. Click on Edit Profile \n 3. Update the details \n 4. Click on Save")
    elif choice2==2:
        print("\n Change my Password: \n 1. Go to Profile \n 2. Click on Change Password \n 3. Enter the old password \n 4. Enter the new password \n 5. Click on Save")
    elif choice2==3:
        print("\n Change my Email Id: \n 1. Go to Profile \n 2. Click on Change Email Id \n 3. Enter the old Email Id \n 4. Enter the new Email Id \n 5. Click on Save")
    elif choice2==4:
        print("\n Change my Phone Number: \n 1. Go to Profile \n 2. Click on Change Phone Number \n 3. Enter the old Phone Number \n 4. Enter the new Phone Number \n 5. Click on Save")
    else:
        print("\n Invalid Input")
elif choice==3:
    print("\n Money Transfer: \n 1. How to transfer money to a bank account \n 2. How to transfer money to a UPI Id \n 3. How to transfer money to a phone number \n 4. How to transfer money to an email id")
    choice3= int(input("Enter the option number: "))
    if choice3==1:
        print("\n Transfer Money to a Bank Account: \n 1. Go to Money Transfer \n 2. Click on Transfer to Bank Account \n 3. Enter the Bank Account Number \n 4. Enter the IFSC Code \n 5. Enter the Amount \n 6. Click on Transfer")
    elif choice3==2:
        print("\n Transfer Money to a UPI Id: \n 1. Go to Money Transfer \n 2. Click on Transfer to UPI Id \n 3. Enter the UPI Id \n 4. Enter the Amount \n 5. Click on Transfer")
    elif choice3==3:
        print("\n Transfer Money to a Phone Number: \n 1. Go to Money Transfer \n 2. Click on Transfer to Phone Number \n 3. Enter the Phone Number \n 4. Enter the Amount \n 5. Click on Transfer")
    elif choice3==4:
        print("\n Transfer Money to an Email Id: \n 1. Go to Money Transfer \n 2. Click on Transfer to Email Id \n 3. Enter the Email Id \n 4. Enter the Amount \n 5. Click on Transfer")
    else:
        print("\n Invalid Input")
elif choice==4:
    print("\n Recharge and Bill Payments: \n 1. How to recharge my phone \n 2. How to pay my electricity bill \n 3. How to pay my water bill \n 4. How to pay my gas bill")
    choice4= int(input("Enter the option number: "))
    if choice4==1:
        print("\n Recharge my Phone: \n 1. Go to Recharge \n 2. Click on Recharge Phone \n 3. Enter the Phone Number \n 4. Enter the Amount \n 5. Click on Recharge")
    elif choice4==2:
        print("\n Pay my Electricity Bill: \n 1. Go to Bill Payments \n 2. Click on Pay Electricity Bill \n 3. Enter the Consumer Number \n 4. Enter the Amount \n 5. Click on Pay")
    elif choice4==3:
        print("\n Pay my Water Bill: \n 1. Go to Bill Payments \n 2. Click on Pay Water Bill \n 3. Enter the Consumer Number \n 4. Enter the Amount \n 5. Click on Pay")
    elif choice4==4:
        print("\n Pay my Gas Bill: \n 1. Go to Bill Payments \n 2. Click on Pay Gas Bill \n 3. Enter the Consumer Number \n 4. Enter the Amount \n 5. Click on Pay")
    else:
        print("\n Invalid Input")
elif choice==5:
    print("\n Reward Refer and Earn: \n 1. How to refer a friend \n 2. How to earn rewards \n 3. How to redeem rewards \n 4. How to check rewards")
    choice5= int(input("Enter the option number: "))
    if choice5==1:
        print("\n Refer a Friend: \n 1. Go to Refer and Earn \n 2. Click on Refer a Friend \n 3. Enter the Friend's Phone Number \n 4. Click on Refer")
    elif choice5==2:
        print("\n Earn Rewards: \n 1. Go to Refer and Earn \n 2. Click on Earn Rewards \n 3. Enter the Amount \n 4. Click on Earn")
    elif choice5==3:
        print("\n Redeem Rewards: \n 1. Go to Refer and Earn \n 2. Click on Redeem Rewards \n 3. Enter the Amount \n 4. Click on Redeem")
    elif choice5==4:
        print("\n Check Rewards: \n 1. Go to Refer and Earn \n 2. Click on Check Rewards \n 3. Enter the Amount \n 4. Click on Check")
    else:
        print("\n Invalid Input")
elif choice==6:
    print("\n Others: \n 1. How to contact customer care \n 2. How to give feedback \n 3. How to report a problem \n 4. How to give suggestions")
    choice6= int(input("Enter the option number: "))
    if choice6==1:
        print("\n Contact Customer Care: \n 1. Go to Contact Us \n 2. Click on Customer Care \n 3. Enter the Query \n 4. Click on Submit")
    elif choice6==2:
        print("\n Give Feedback: \n 1. Go to Contact Us \n 2. Click on Feedback \n 3. Enter the Feedback \n 4. Click on Submit")
    elif choice6==3:
        print("\n Report a Problem: \n 1. Go to Contact Us \n 2. Click on Report a Problem \n 3. Enter the Problem \n 4. Click on Submit")
    elif choice6==4:
        print("\n Give Suggestions: \n 1. Go to Contact Us \n 2. Click on Give Suggestions \n 3. Enter the Suggestions \n 4. Click on Submit")
    else:
        print("\n Invalid Input")
else:
    print("\n Invalid Input")
print("\n Thank you for using the chatbot. Have a great day ahead.")


os.system('say "Thank you for using our chatbot, Have a great day ahead"')
