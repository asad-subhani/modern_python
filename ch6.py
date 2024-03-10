messages:list[str] = ["Hello there.", "This is ASR."]
sentMesgs:list[str] = []
def send_messages(mesgs:list[str], sent:list[str])->None:
  num:int = 1
  for msg in mesgs:
    print(num)
    num+=1
    sent.append(msg)
    print(f"Sending message: {msg}")
    mesgs.remove(msg)

def showMesg(mesgs:list[str])->None:
  for mesg in mesgs:
    print(mesg)


print(messages)

send_messages(mesgs= messages[:], sent=sentMesgs)
print(sentMesgs)
print("\nFollowing messages has been sent.")
showMesg(sentMesgs)