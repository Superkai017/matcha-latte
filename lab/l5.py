def mask_credit_card(card_number):
    if len(card_number) < 4:
        return "Invalid card number"
    return "*" * (len(card_number) - 4) + "-" + card_number[-4:]
print(mask_credit_card("1234-5678-1234-5678"))