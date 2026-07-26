# ============================================
# Python Data types  Demonstration
# Refrerence : Chhatrapati Shivaji Maharaj (Historical Data)
# ============================================

# 1. Integer (Int) - Represents whole numbers 
janm_varsh = 1630
rajyabhishek_varsh = 1674

# 2. string (str) - represent text
naav = "Chhatrapati Shivaji Shahaji Bhosale Maharaj"
title = "Chhatrapati"
janm_sthal = "Shivneri Fort, Junnar, Pune, Maharashtra, India"

# 3. Boolean (bool) - Represents True or False logical values
swarajya_sthapna_zali = True

# 4. List (list) - Ordered, mutable collection of items
pramukh_kille = ["Raigad Fort", "Rajgadh Fort", "Sindhudurg Fort", "Pratapgad Fort", "Torna Fort"]

# 5. Tuple (tuple) - Ordered, immutable collection of items
rajyabhishek_details = ("6 June 1674", "Raigad Fort", "Chhatrapati Shivaji Maharaj")

# 6. Dictionary (dict) - Key- Values pair mapping
ch_shivaji_maharaj_info = {
    "Naav": naav,
    "Title": title,
    "Janm Varsh": janm_varsh,
    "Janm Sthal": janm_sthal,
    "Rajyabhishek Varsh": rajyabhishek_varsh,
    "Swarajya Sthapna Zali": swarajya_sthapna_zali,
    "Pramukh Kille": pramukh_kille,
    "Rajyabhishek Details": rajyabhishek_details
}

"""
============================================
Output Section
============================================
"""
print("======Histrocal Data of Chhatrapati Shivaji Maharaj======")
for key, value in ch_shivaji_maharaj_info.items():
    print(f"{key}: {value}")

print("\n======Data Type Verification======")
print(f"Type of janm_varsh: {type(janm_varsh)}")
print(f"Type of naav: {type(naav)}")
print(f"Type of swarajya_sthapna_zali: {type(swarajya_sthapna_zali)}")
print(f"Type of pramukh_kille: {type(pramukh_kille)}")
print(f"Type of rajyabhishek_details: {type(rajyabhishek_details)}")
print(f"Type of ch_shivaji_maharaj_info: {type(ch_shivaji_maharaj_info)}")

