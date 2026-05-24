from flask import Flask,request,render_template
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return("welcome to home page ")

@app.route('/image',methods =['GET','POST'])
def image():
    if request.method == 'GET':
        return render_template('index.html',result = None)
    else:
        save_dir ="images"

        os.makedirs(save_dir,exist_ok = True)
        
        query ="emmanuel macron"
        headers = {
                "User-Agent": "Mozilla/5.0"
            }

        url = requests.get(f"https://www.google.com/search?sca_esv=4eed9403753dc5f1&rlz=1C1RXQR_enIN1152IN1152&sxsrf=ANbL-n6wosB1MpDpwX_adwFUHRJzEgVbAA:1771827970407&udm=2&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKp0UJuhqwKhR0QUhF54-6jIYFfWbU_Clyew-1Wh7zkL7FFfeQ8UTZRt91soqZupfwPo0crig5A2MrUrvJfjH7QciSH8xUwQHQ9E5ErbsMbM8TE-vSnoDz0uiGZY2lFFSUOY9YcktIMaOamWoIYoq_K39QHv1JgkGPARMooT83wM_fA1Z7IQJUEzhMYSXrprIOMkBHVHg&q=emmanuel+macron&sa=X&ved=2ahUKEwj9z53G_e6SAxViQ2cHHZHzKSEQtKgLegQIEhAB&cshid=1771828024834859&biw=1024&bih=486&dpr=3.75",headers=headers)




        soup=BeautifulSoup(url.content,"html.parser")



        image_tags = soup.find_all("img")

        del image_tags[0]
        

        for index,i  in enumerate(image_tags):
            image_src = i['src']
            image_data = requests.get(image_src).content
            # image_data = 
            with open(os.path.join(save_dir,f"{index} _ {query} .jpg"),'wb')as f:
                f.write(image_data)

        
        return render_template('index.html',result =f"images_loded succesfully for {query}")
        
        





if __name__ =='__main__':
    app.run(debug =True)