import google.generativeai as genai

def getAIData(data):
    API_KEY = "AIzaSyDxcb015CoMUecOwUeZ37C_u_c2PV8-2NQ"
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Explain this in terms of trends: {data}. The data is about covid 19 cases. Also mention some precautions so that nothing like this can spread rapidly if anything like this occurs once again. Also compare the covid 19 dataset with the newly emerging hmpv virus")
    return response.text

def secondFun(data):
    API_KEY = "AIzaSyDxcb015CoMUecOwUeZ37C_u_c2PV8-2NQ"
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Explain this in terms of trends: {data}. The data is about covid 19 cases. Show the comparison of growth rates in 3 months percentage in bold. I NEED NUMBERSSSS DO ANYTHING BUT I NEED NUMBERS. DO YOUR CALCULATIONS OR ANYTHIUNG I DONT CARE")
    return response.text