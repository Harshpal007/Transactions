# Transactions

## Deployment

To deploy this project run

```bash
  python3 -m venv virtualenv  
  source virtualenv/bin/activate
  pip install -r requirements.txt
```
## API Reference

#### Get Block Number from number

```http
  POST /api/block-number/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `input_number` | `integer` | **Required**. Input Number provided by user |

#### Get item

```http
  GET /api/transactions/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `input_number`      | `integer` | **Required**. Input Number provided by user |
| `block_number`      | `string` | **Required**. Block Number got in response from the previous API |


