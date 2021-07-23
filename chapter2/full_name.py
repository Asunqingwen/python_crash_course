first_name = "ada"
last_name = "lovelace"
# full_name = "{} {}".format(first_name,last_name) #python3.5
full_name = f"{first_name} {last_name}"  ## f为format的简写,python3.6引入
print(full_name)
message = f"Hello,{full_name.title()}!"
print(message)
