class Item:

    def __init__(self, date, product, quantity):
        self.date = date
        self.product = product
        self.quantity = int(quantity)

    def __str__(self):
        return (f"- {self.date}: {self.quantity}\n")

def generate_product_report(data):
    """Ваш код"""
    hash_map = {}
    strings = data.split(';')
    for s in strings:
        locals_strings = s.split(':')
        if locals_strings[1] in hash_map:
            hash_map[locals_strings[1]].append(
                Item(locals_strings[0],"",locals_strings[2])
            )
        else:
            hash_map[locals_strings[1]] = []
            hash_map[locals_strings[1]].append(
                Item(locals_strings[0],"",locals_strings[2])
            )
    answer = []
    for key, value in hash_map.items():
        tmp = f"{key}:\n"
        for v in value:
            tmp += str(v)            
    return answer


input_data =  input()
product_report_generator = generate_product_report(input_data)
print(product_report_generator)
for report in product_report_generator:
    print(report)