from flask import Flask, request, render_template, jsonify,send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from Temporary import *
import os
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication
#app.config['MAX_CONTENT_LENGTH']=250*1024*1024



@app.route("/encrypt")
def encryption():
    os.system("rm -rf temp/*.*")
    #print("Hello")
    return render_template("encryption.html")

@app.route("/decrypt")
def decryption():
    os.system("rm -rf temp/*.*")
    #print("Hello")
    return render_template("decryption.html")











@app.route("/download/<filename>")
def download(filename):
    return send_from_directory("./temp/", filename, as_attachment=True)



@app.route("/")
def upload_file():
    os.system("rm -rf temp/*.*")
    #print("Hello")
    return render_template("index.html")



@app.route("/uploader/", methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
            
        opt = "1"
        content={}
        message="Operation Performed"

        
        #Input type Text or File
        if request.form.get('ipmode')=="text":
            dt="1"
            iptext=request.form.get('iptext')
            content.update({'iptext':iptext})
        elif request.form.get('ipmode')=="file":
            dt="2"
            f = request.files['ipfile']
            fname = secure_filename(f.filename)

            f.save(os.getcwd()+'/temp/' + fname)
            content.update({"fname":fname})
        

        #Encryption Mode simple or advanced
        mode=request.form.get('mode')
        if mode=="simple":
            m="1"
            alg=request.form.get('algorithm')
            blocksize=request.form.get('blocksize')
            keysize=request.form.get('keysize')
            content.update({"alg":alg,"blocksize":blocksize,"keysize":keysize})
        elif mode=="advanced":
            m="2"
            alg=request.form.get('algorithm')
            blocksize=request.form.get('blocksize')
            keysize=request.form.get('keysize')
            ivect=request.form.get('iv')
            kvalue=request.form.get('kvalue')
            content.update({"alg":alg,"blocksize":blocksize,"keysize":keysize,"ivect":ivect,"kvalue":kvalue})

        content.update({'dt':dt})
        content.update({'m':m})
        content.update({'opt':opt})

        retval = cryptomain(content)
        #hexData = os.system("cat ./temp/"+retval["encryptedHexFile"])
        #print(hexData)




        #if name =='admin':
        #    return redirect(url_for('download',filename = name))




        #tempval= retval["encryptedFile"]
        #retval["encryptedFile"] = request.host_url + "temp/"+ tempval
        #print(retval["encryptedFile"])

        #tempval= retval["encryptedHexFile"]
        #retval["encryptedHexFile"] = request.host_url + "temp/"+ tempval
        #print(retval["encryptedHexFile"])

        
        if retval not in [401,402,403]:
            message = "Encryption Performed Successfully"
        
        
        return jsonify({"Data":retval})













#Decryption Url
@app.route("/downloader/", methods = ['GET', 'POST'])
def downloader():
    if request.method == 'POST':
            
        opt = "2"
        content={}
        message="Operation Performed"

        
        #Input type Text or File
        if request.form.get('ipmode')=="text":
            dt="1"
            iptext=request.form.get('iptext')
            content.update({'iptext':iptext})
        elif request.form.get('ipmode')=="file":
            dt="2"
            f = request.files['ipfile']
            fname = secure_filename(f.filename)

            f.save(os.getcwd()+'/temp/' + fname)
            content.update({"fname":fname})
        

        #Encryption Mode simple or advanced
        mode=request.form.get('mode')
        if mode=="simple":
            m="1"
            alg=request.form.get('algorithm')
            blocksize=request.form.get('blocksize')
            keysize=request.form.get('keysize')
            kvalue=request.form.get('kvalue')
            content.update({"alg":alg,"blocksize":blocksize,"keysize":keysize, "kvalue":kvalue})
        elif mode=="advanced":
            m="2"
            alg=request.form.get('algorithm')
            blocksize=request.form.get('blocksize')
            keysize=request.form.get('keysize')
            ivect=request.form.get('iv')
            kvalue=request.form.get('kvalue')
            content.update({"alg":alg,"blocksize":blocksize,"keysize":keysize,"ivect":ivect,"kvalue":kvalue})

        content.update({'dt':dt})
        content.update({'m':m})
        content.update({'opt':opt})

        retval = cryptomain(content)
        if retval not in [401,402,403]:
            message = "Decryption Performed Successfully"


        
        
        return jsonify({"Data":retval})






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
