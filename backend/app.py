from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# 配置資料庫
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testpoints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 定義資料模型
class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    test_items = db.relationship('TestItem', backref='module', lazy=True)

class TestItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    test_points = db.relationship('TestPoint', backref='test_item', lazy=True)

class TestPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    test_item_id = db.Column(db.Integer, db.ForeignKey('test_item.id'), nullable=False)

# 創建資料表
with app.app_context():
    db.create_all()

# API路由
@app.route('/api/modules', methods=['GET'])
def get_modules():
    modules = Module.query.all()
    return jsonify([{
        'id': module.id,
        'name': module.name,
        'description': module.description
    } for module in modules])

@app.route('/api/modules', methods=['POST'])
def create_module():
    data = request.get_json()
    new_module = Module(
        name=data['name'],
        description=data.get('description', '')
    )
    db.session.add(new_module)
    db.session.commit()
    return jsonify({'id': new_module.id, 'name': new_module.name}), 201

@app.route('/api/modules/<int:module_id>/test-items', methods=['GET'])
def get_test_items(module_id):
    test_items = TestItem.query.filter_by(module_id=module_id).all()
    return jsonify([{
        'id': item.id,
        'name': item.name,
        'description': item.description
    } for item in test_items])

@app.route('/api/test-items', methods=['POST'])
def create_test_item():
    data = request.get_json()
    new_item = TestItem(
        name=data['name'],
        description=data.get('description', ''),
        module_id=data['module_id']
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'id': new_item.id, 'name': new_item.name}), 201

@app.route('/api/test-items/<int:item_id>/test-points', methods=['GET'])
def get_test_points(item_id):
    test_points = TestPoint.query.filter_by(test_item_id=item_id).all()
    return jsonify([{
        'id': point.id,
        'content': point.content
    } for point in test_points])

@app.route('/api/test-points', methods=['POST'])
def create_test_point():
    data = request.get_json()
    new_point = TestPoint(
        content=data['content'],
        test_item_id=data['test_item_id']
    )
    db.session.add(new_point)
    db.session.commit()
    return jsonify({'id': new_point.id, 'content': new_point.content}), 201

if __name__ == '__main__':
    app.run(debug=True) 