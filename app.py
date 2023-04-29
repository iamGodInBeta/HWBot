from fastapi import FastAPI ,Request
import httpx
import json

app = FastAPI()

token = "6143957998:AAFiE9fiXPLrjtZQXuAvNC_QKHKwfULplIg"
BASE_URL = f"https://api.telegram.org/bot{token}"
def req_info (son):
	media_types = media_types = ['animation','audio','document','photo','video','video_note','voice','sticker','text']
	print(json.dumps(son,indent = 4, sort_keys=True))
	for i in media_types:
		if i in son:
			if i == 'photo':
				path = son[i][0]["file_id"]
			elif i == "text":
				path=son['text']
			else:
				path = son[i]["file_id"]
			return [i,path,son["chat"]["id"]]
	return None
			
			
			
async def return_back (filetype,usr,path_id):
	print(filetype.capitalize())
	client = httpx.AsyncClient()
	payload = {'chat_id':usr,filetype:path_id}
	if filetype == "text":
		filetype = "Message"
	print(payload)
	url = f'{BASE_URL}/send{filetype}'
	print(url)
	await client.get(url,params = payload)
	
@app.post("/webhook/")
async def webhook(req:Request):
	data = await req.json()
	message = data["message"]
	#pretified json output
	# ~ loaded = json.dumps(message,indent = 4, sort_keys=True)
	parsed_info = req_info(message) 
	if parsed_info == None:
		print("none")
	else:
		file_type = parsed_info[0]
		file_id = parsed_info[1]
		usr_id = parsed_info[2]
		await return_back(file_type,usr_id,file_id)
	return data
	



