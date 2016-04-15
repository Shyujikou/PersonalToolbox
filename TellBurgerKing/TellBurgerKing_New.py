from splinter import Browser
import re, sys

# Ask user to input the 16-digit receipt number and format the entry data string
rn = raw_input('Receipt Number: ')
if not re.match(r"\d{16}", rn):
    print 'Receipt number must be a 16-digit number.'
    exit()
rns = [rn[i:i+3] for i in range(0, len(rn), 3)]

b = Browser('phantomjs')

sys.stdout.write('.')
sys.stdout.flush()
b.visit('https://tellburgerking.com.cn/')
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
b.fill('CN1', rns[0])
b.fill('CN2', rns[1])
b.fill('CN3', rns[2])
b.fill('CN4', rns[3])
b.fill('CN5', rns[4])
b.fill('CN6', rns[5])
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//div[@class='Opt2 rbloption']/span/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//div[@class='Opt1 rbloption']/span/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt5 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt5 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt5 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt5 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt5 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt2 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt5 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt5 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//div[@id='FNSR000082']/span/span[@class='checkboxBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//div[@id='FNSR000097']/span/span[@class='checkboxBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt5 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt5 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt5 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt5 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//td[@class='Opt1 inputtyperbloption']/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//div[@class='Opt1 rbloption']/span/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//div[@class='Opt1 rbloption']/span/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
for e in b.find_by_xpath("//div[@class='Opt1 rbloption']/span/span[@class='radioBranded']"):
    e.click()
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
b.select('R069000', '9')
b.select('R070000', '9')
b.find_by_id('NextButton').click()

sys.stdout.write('.')
sys.stdout.flush()
b.find_by_id('NextButton').click()

print b.find_by_xpath("//p[@class='ValCode']").first.value
b.quit()

anykey = raw_input()
