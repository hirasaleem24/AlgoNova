#!/bin/bash
echo "🚀 Setting up AlgoNova environment..."

cd backend
pip install -r requirements.txt

cd ../frontend
npm install

echo "✅ Setup complete! Run backend with: uvicorn main:app --reload"
echo "   Then start frontend: npm start"
