python3 -m venv ./venv
ls
source ./venv/bin/activate  //kích hoạt môi trường
pip install fastapi
pip install uvicorn
pip freeze
code requirements.txt       //tạo file requirements.txt
    fastapi~=0.111.0        //~ tự động nâng cấp nếu cần nhưng chỉ là bản vá
    uvicorn~=0.29.0
pip install -r requirements.txt     //cài theo file requirements

mkdir app
cd app
l
➜  app touch __init__.py
➜  app touch main.py

➜  app uvicorn main:app --reload
    {"Hello":"World"}

➜  app cd ..
➜  k8s-getting-started docker build .  
➜  k8s-getting-started docker build -t k8s-fast-api .      //thêm tag
➜  k8s-getting-started docker run -p 8000:80 k8s-fast-api
➜  k8s-getting-started docker build -t shinichiok2614/k8s-getting-started:0.0.1 .
➜  k8s-getting-started docker push shinichiok2614/k8s-getting-started:0.0.1

https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

➜  kubernetes touch deployment.yaml

https://kubernetes.io/docs/concepts/services-networking/

23:26

echo "# k8s-civo-python" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:shinichiok2614/k8s-civo-python.git
git push -u origin main

git remote add origin git@github.com:shinichiok2614/k8s-civo-python.git
git branch -M main
git push -u origin main