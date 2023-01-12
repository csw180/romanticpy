GIT 설치 및 환경설정
===================
###### 원문 : https://hackmd.io/@oW_dDxdsRoSpl0M64Tfg2g/ByfwpNJ-K

1. Git 설치하기  : <https://git-scm.com/>
2. 설치완료후 Git bash 열기
3. git bash 에서 환경설정하기            
>  3.1 Step1 : 유저이름 설정
```
git config --global user.name "your_name"
```
>  3.2 Step2 : 유저 이메일 설정
```
git config --global user.email "your_email"
```
* Github가입시 사용한 이메일을 써주세요!

>  3.3 Step3 : 정보확인하기
```
git config --list
```

Github 처음 코드 업로드하기
===================

1. 초기화
```
git init
```
2. 추가할 파일 더하기
```
git add .
```
* 특정파일을 선택해서 올리고 싶으면  git add index.html
3. 상태확인하기
```
git status
```
4. 히스토리 만들기
```
git commit -m "first commit"
```
5. Github repository랑 내 로컬 프로젝트랑 연결
```
git remote add origin https://github.com/bitnaGithub/firstproject.git
```
* git URL 은 github 에서 복붙
6. 잘 연결됬는지 확인 (선택사항)
```
git remote -v
```

Github 에 계속 업데이트 하는 법
===================
1. 추가할 파일 더하기
```
git add .
```
2. 히스토리 만들기
```
git commit -m "second commit"
```
3. Github 올리기
```
git push origin master
```
* 내 컴퓨터에 소스코드를 업데이트를 하고 싶으면 이 세개의 스텝만 계속 반복하면 됨

Github 로 팀프로젝트 하는 법
===================
1. Github에서 소스코드 다운로드
```
git clone 주소 폴더이름
```
* 주소는 깃허브에서 들고와야함
* 폴더이름은 선택사항이다 (즉 없어도됨) 폴더이름을 줄경우에는 그 폴더가 새로 생성이 되면서 그 안에 코드들이 다운로드가 되고, 폴더이름을 안줄경우엔 깃허브 프로젝트 이름으로 폴더가 자동으로 생기고 그안에 코드들이 다운로드된다.

2. Github에서 내 브렌치(branch) 만들기
```
git checkout -b 브렌치이름
```
3. 내 브렌치에 소스코드 업데이트 하기
```
git add .
git commit -m "first commit"
git push origin 브렌치이름
```
4. 마스터 브렌치에서 소스 가져오기(pull)
```
git pull origin master
```
* pull을 하기전에는 기존에 소스코드들을 commit을 먼저 해놔야 한다 (2탄 강의참조)
5. 브렌치끼리 이동하는 법
```
git checkout 브렌치이름
```
* 강의에서 소개하진 않았지만 내가 내 브렌치에서 마스터 브렌치로 이동을 하고 싶거나 다른 브렌치로 이동하고싶으면 해당 명령어를 쓰면 된다

