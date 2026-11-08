# Vũ điệu cây xanh - Sứa Taho

Deployment-only branch. Full game archive is stored as sequential binary chunks under `chunks/`.
Render Build Command:

```
cat chunks/*.part > game.zip && unzip -qo game.zip && cd vu-dieu-cay-xanh && npm install --omit=dev
```

Render Start Command:

```
cd vu-dieu-cay-xanh && npm start
```

Health endpoint: `/api/health`.
