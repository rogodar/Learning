text = "X-DSPAM-Confidence: 0.8475"
num = text.find(':')
pnum = text[num+2:]
endNum = float(pnum)
print(endNum)