
print('creating collection and user/pwd')

db = db.getSiblingDB('api-db');
db.createCollection('user');
db.createUser(
  {
    user: 'svc_api',
    pwd: 'svc_api_password',
    roles: [{ role: 'readWrite', db: 'api-db' }],
  },
);

print('user/paswd and collection created')