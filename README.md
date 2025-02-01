# Djangoの Template 利用方法の練習

## 📌 概要
このプロジェクトは、Django の **View と Template の連携** を学ぶための練習用アプリケーションです。

本プロジェクトは、以下の Udemy コースのセッション6をベースに実装しました：
📚 [Python + Django5 Djangoを基礎から応用まで、アプリケーション開発マスターpython付き](https://www.udemy.com/share/103OHY3@5JdSpwpJtBk6FXDdLoQeB-D1g_nt31JH7eSso0Ld1otnAfjP6jSbJjPZHRQXrwCRsA==/)

**学習ポイント**
- Django の **View と Template の基本的な連携**
- **動的なHTMLテンプレートの活用**
- **Django のプロジェクト構造の理解**
- **基本的なルーティングとビューの実装**

---

## 🛠️ 使用技術
- **フレームワーク**: Django 5
- **データベース**: SQLite
- **フロントエンド**: HTML / CSS
- **開発環境**: Python 3.x, Django Shell
- **仮想環境**: venv

---

## 🚀 実行方法

### 1️⃣ **リポジトリをクローン**
```bash
git clone https://github.com/chaizhiyuan2501/TemplateExam.git
cd TemplateExam
```

### 2️⃣ **仮想環境の作成と有効化**
**Windows (PowerShell) の場合**
```powershell
python -m venv venv
.\venv\Scripts\Activate
```
**Windows (\u30b3マンドプロンプト) の場合**
```cmd
venv\Scripts\activate.bat
```
**Mac / Linux の場合**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ **必要なパッケージをインストール**
```bash
pip install django
```

### 4️⃣ **サーバーの起動**
```bash
python manage.py runserver
```

---

## 🎯 動作確認
ブラウザで以下のURLにアクセスしてアプリの動作を確認します：
🔗 **http://127.0.0.1:8000/app/home**

---
