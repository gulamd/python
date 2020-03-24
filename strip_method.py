name = "        GulamRasool        "
dots = "......................."
#lstrip() methid to remove space from left side 
print(name + dots)
print(name.lstrip() + dots)
#rstrip( method to use for removing the right sid espace)
print(name.rstrip() + dots)
#strip() use for remove the left and right side space
print(name.strip() + dots)
# remove the space between the variable "use replace()"method
tree = "gulam      rasool"
print(tree.replace(" ","") + dots)