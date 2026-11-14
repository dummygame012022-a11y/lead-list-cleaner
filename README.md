# Lead List Cleaner

Python script nga naglimpyo sa gubot nga CSV sa mga lead (kompanya, email, website, phone).

## Unsa ang gibuhat
- Tangtang ang duplicate
- Limpyohan ang gap ug letra sa ngalan
- I-check kung husto ang email ug phone
- Butangan og https:// ang website
- Markahan ang walay sulod o sayop (status column)
- Mo-save og clean.csv ug report.txt

## Before
    JUAN STORE  ,juanstore@gmail,www.site.com,0917 123 4567
    Ana Pharmacy,,,123

## After
    Juan Store,juanstore@gmail,https://www.site.com,09171234567,sayop email
    Ana Pharmacy,,,123,"walay email, walay website, sayop phone"

## Sample nga resulta
    Total: 68 | Duplicate nga gitangtang: 44 | Limpyo: 24
    Website giayo: 10 | Sayop email: 9 | Sayop phone: 15

## Unsaon pagpadagan
    python make_data.py   (himo og peke nga messy.csv)
    python cleaner.py     (himo og clean.csv ug report.txt)

Peke ang data. Python 3 ra, walay dugang nga i-install.
