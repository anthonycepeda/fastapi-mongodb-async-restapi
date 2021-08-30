
print('creating collection and user/pwd')

// db = db.getSiblingDB('api-db');
db.createCollection('api-db');
db.createUser(
  {
    user: 'svc_api',
    pwd: 'svc_api_password',
    roles: [{ role: 'readWrite', db: 'api-db' }],
  },
);

print('user/paswd and collection created')