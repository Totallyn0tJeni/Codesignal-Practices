gadget_list = ["smartphone", "camera", "power bank", "headphones"]
packed_gadgets = ["smartphone", "power bank", "headphones"]

for gadget in gadget_list:
    if gadget not in packed_gadgets:
        print(f"Forgot to pack {gadget}")
        break
