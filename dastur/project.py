
from dastur.auth import register, login
from dastur.product import create_cat, cat_list, create_product, expinsive_price, cheap_price, guruh_b


#1 register royxatdan otish+
# 2 login qilish+
#3 admin va userni farqlash +
#4 Admin uchun
# I category qoshish
# II product qoshish
# III eng qimmat product
# IV eng orzon product
# V product o'zgartirish
# VI product o'chirish
# 5 User uchun
# I ro'yxatdan otish'
# II login qilish
# III cat ni korish
# IV productlarni korish
# V sotib olish



def main():
    print("""
    1 register
    2 login""")
    while True:
        user_answer=input("Tanlang:")
        if user_answer == "1":
            username = input("Username:")
            address = input("Address:")
            password = input("Password:")
            register(username, address,password)
        elif user_answer == "2":
            username = input("Username:")
            password = input("Password:")
            user=login(username,password)
            if user[-1]:
                while True:
                    print("""
                    1 category qoshish
                    2 product qoshish
                    3 eng qimmat product
                    4 eng orzon product
                    5 product o'zgartirish
                    6 product o'chirish""")
                    user_ch=input("Enter your choice:")
                    if user_ch == "1":
                        title = input("Enter your title:")
                        create_cat(title)
                    elif user_ch == "2":
                        cat_list()
                        title = input("Enter your title:")
                        price = input("Enter your price:")
                        description = input("Enter your description:")
                        quantity = int(input("Enter your quantity:"))
                        cat_id = input("Enter your category id:")
                        create_product(title, price, description, quantity, cat_id)
                    elif user_ch == "3":
                        m=expinsive_price()
                        print(m)
                    elif user_ch == "4":
                        print(cheap_price())
                    elif user_ch == "5":
                        print(guruh_b())




main()


