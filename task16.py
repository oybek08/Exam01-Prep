asosiy_narx = 100000
yosh = 5

if yosh <= 7:
    chegirma_foizi = 50
elif yosh <= 18:
    chegirma_foizi = 30
elif yosh >= 60:
    chegirma_foizi = 40
else:
    chegirma_foizi = 0

chegirma_miqdori = asosiy_narx * chegirma_foizi / 100
yakuniy_narx = asosiy_narx - chegirma_miqdori

print(f"Yakuniy narx: {int(yakuniy_narx)} so'm ({chegirma_foizi}% chegirma qo'llanildi)")
