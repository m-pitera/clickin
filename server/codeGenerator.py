import random
import string


BAD_WORDS = ["ass","fuc","fuk","fuq","fux","fck","coc","cok","coq","kox","koc","kok","koq","cac","cak","caq","kac","kak","kaq","dic","dik","diq","dix","dck","pns","psy","fag","fgt","ngr","nig","cnt","knt","sht","dsh","twt","bch","cum","clt","kum","klt","suc","suk","suq","sck","lic","lik","liq","lck","jiz","jzz","gay","gey","gei","gai","vag","vgn","sjv","fap","prn","lol","jew","joo","gvr","pus","pis","pss","snm","tit","fku","fcu","fqu","hor","slt","jap","wop","kkk","kik","kyk","kyc","kyq","dyk","dyq","dyc","kkk","jyz","prk","prc","prq","mic","mik","miq","myc","myk","myq","guc","guk","guq","giz","gzz","sex","sxx","sxi","sxe","sxy","xxx","wac","wak","waq","wck","pot","thc","vaj","vjn","nut","std","lsd","poo","azn","pcp","dmn","orl","anl","ans","muf","mff","phk","phc","phq","xtc","tok","toc","toq","mlf","rac","rak","raq","rck","sac","sak","saq","pms","nad","ndz","nds","wtf","sol","sob","fob","sfu"]

def generateCode(numOfChars):
    urlBase = "click.in/"
    code = ""

    while(not isValid(code.lower())):
        code = generateRandomElems(numOfChars)

    return code

def generateRandomElems(numOfChars):
    POSSIBLE_CHARS = string.ascii_letters + string.digits
    code = ""

    for x in range(numOfChars):
        randomElem = random.choice(POSSIBLE_CHARS)
        code += randomElem

    return code

def isValid(code):
    return code or not(BAD_WORDS in code)