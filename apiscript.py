import requests
import json
import pandas as pd
import csv

# Токен аутентификации
Bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJZVGdpdHBCcDhJUXkyWjJEQVc5MTh4ZWlqZHJKMHFnNExNWHNQLUZKTHZJIn0.eyJleHAiOjE3MTEwNDQ0NTQsImlhdCI6MTcxMTAwODQ1NywiYXV0aF90aW1lIjoxNzExMDA4NDU0LCJqdGkiOiJiZTlhOTAxMS1kZGRkLTQ1YjQtYTA4ZS02NTYwNWE3NWIyMzMiLCJpc3MiOiJodHRwOi8va2V5Y2xvYWsuZnBwZC5wcC5hb3J0aS50ZWNoL2F1dGgvcmVhbG1zL0ZQUERfZXh0ZXJuYWxfdXNlcnMiLCJhdWQiOlsiZnBwZC1wZXJzLWRhdGEiLCJGUFBEX0xLX0RFViIsImFjY291bnQiXSwic3ViIjoiY2Y3ZGIzMGUtYmYyMy00NjRjLWJkZDktMDhiZGQ4YjY5MzMyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiRlBQRF9MS19ERVYiLCJub25jZSI6ImQ4MGFlNmI5LWVlMzAtNGFhNS1hZjMxLWM1MzAzMjE2ZjdmMCIsInNlc3Npb25fc3RhdGUiOiIyMzIyMDZhMC1hNzliLTQyNWEtOGE2Yi1lNTFiNzI2ZDMxOTciLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbImh0dHA6Ly9say5mcHBkLnBwLmFvcnRpLnRlY2giLCJodHRwOi8vcG9ydGFsLmZwcGQucHAuYW9ydGkudGVjaCIsImh0dHA6Ly9hcC1wZXJzLWRhdGEtY3JlYXRlci5mcHBkLnBwLmFvcnRpLnRlY2giLCJodHRwOi8vZnBwZC1say5mcHBkLnBwLmFvcnRpLnRlY2giLCJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJodHRwOi8vMTcyLjIzLjE2OS40NDo0MjAwIiwiaHR0cDovLzE3Mi4yMy4xNjkuMTY6NDIwMCIsImh0dHA6Ly9yLWFwLXBlcnMtZGF0YS1jcmVhdGVyLmZwcGQucHAuYW9ydGkudGVjaCIsImh0dHA6Ly9yLWZwcGQtbGsuZnBwZC5wcC5hb3J0aS50ZWNoIiwiaHR0cDovL2ZwcGQtbGstZGV2LmZwcGQucHAuYW9ydGkudGVjaCIsImh0dHA6Ly9sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9yLWxrLmZwcGQucHAuYW9ydGkudGVjaCJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZnJlZWlwYSBGUFBEX0xLX0RFViBlbWFpbCIsInBlcnNEYXRhVXNlcklkIjoiNjg3ZWQ5ZGYtZWUyMi00OTJlLTg3YTItMjZmY2RmZmRkYTFhIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoi0JrQvtGA0L3QuNC7INCU0L7QvNC-0LLQtdGA0L7QsiIsImdyb3VwcyI6WyIvYWRtaW5zX2ZwcGRfc2kiLCIvMDdmMWE4ZDYtMGY2YS00ZGNhLThhYzktNjc1YWRmNzQ5MTI3IiwiL2ZwcGQtbWQtYWRtaW4iLCIvZnBwZC1ucmktYWRtaW5pc3RyYXRvciIsIi8xZDkxNmM2My02ZDI5LTQ1NGQtYjBhZi1kODE1ODExNmQ0ZDUiLCIvMjAyMzhlNjQtMjY2Zi00ZDU2LWFkYmMtMjZiMWNiNWE1ZjkxIiwiL2ZwcGQtaHMtb3BlcmF0b3IiLCIvYTk4MzM0ODAtNGU0Ny00Y2VjLTljNTktZjllNmZhY2Y2MDdmIiwiL2ZwcGQtb3otc3RhdGVtZW50X3Byb2MiLCIvdGVzdDMzMzExMSIsIi84MjM5MWZiMy1kNGQzLTQ0ZDYtOGMwMi01YzQzNDNjNjUzZDgiLCIvYWRtaW5zX2ZwcGRfYXAiLCIvNzkxMzZkNGYtZmMwYS00MzQzLWEyYzQtNTNmNWU3ZjQ5NWZmIiwiL2ZwcGQtb3otc3RhdGVtZW50X3Byb2NfY2hpZWYiLCIvZnBwZC11YS1leHRlcm5hbHVzZXJzIiwiL2FkbWluc19vcG1kIiwiL2ZwcGQtaHMtdXNlciIsIi9mcHBkLXVhLWFkbWluaXN0cmF0b3IiLCIvZnBwZC1vei1jb250cmFjdF9wcm9jIiwiL2ZwcGQtdWEtaW50ZXJuYWx1c2VycyIsIi9mcHBkLW1kLWV4dC1wcm92aWRlciIsIi9mcHBkLXZsay1tb25pdG9yaW5nIiwiL2ZwcGQtaHMtYWRtaW5pc3RyYXRvciJdLCJmcmVlSXBhSWQiOiIwMDAwMDA2MDAwNCIsInByZWZlcnJlZF91c2VybmFtZSI6IjAwMDAwMDYwMDA0IiwiZ2l2ZW5fbmFtZSI6ItCa0L7RgNC90LjQuyIsImZhbWlseV9uYW1lIjoi0JTQvtC80L7QstC10YDQvtCyIiwiZW1haWwiOiIwMDAwMDA2MDAwNEBwcC5hb3J0aS50ZWNoIn0.IQF5h-ivN0dXQx-buT8LJkxfwW5CjeNiSG9vPGoUKUXuAunGE5h3aYHO2cVB334fABKL8Gt_MvWgeR8hDOqh_yVsaNebUcIF2uT9NsohTqb0TMe27Kn7nYNQKOMp3x_NP1eYjI0XhmDd8CriSL3_9Sft5qaZMDjpHDwaia1bdvhFYXaO2PclBiWMzFqf7hequi-2ltck-_hlS2MZ6CZAXzvaxR10FaNDgGc9P_2x9GBIazGykvuQ-wQJPBg4cgFI4areUSoQ-LNZ6s40aljpQCWxzNQ09miRa0bpWY92TSo_V3OxLY-XV-qjBcUtfpFb2-GxPwcAtzFvDdN87iZLNA'" 

# URL
BASE_URL = 'http://lk.fppd.pp.aorti.tech/fppd-md/dictionary/Scale?group_ref='

# Поле, по которому искать 
field = 'name'

# Поле, которое нужно достать
data_field = 'id'

heads = {'Authorization': f'{Bearer_token}'}
df = pd.read_csv('names.csv', sep=';') # CSV файл со списком полей, по которым необходим поиск, разделитель: ';'
names_dict = df.to_dict()

df = pd.read_csv('ids.csv', sep=';') # CSV файл со списком, разделитель: ';'
ids_dict = df.to_dict()

res_dict = {"user_id": 0}
res_dict.update(names_dict)
with open('results.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, res_dict.keys(), delimiter=';')
    w.writeheader()

    for guid in ids_dict.keys():
        res_dict[f'{field}'] = guid
        response = requests.get(f"{BASE_URL}{guid}", headers = heads) ### Ссылка GET запроса
        json_dict = json.loads(response.text)
        for obj in json_dict:
            if obj[f'{field}'] in res_dict:
                res_dict[obj[f'{field}']] = obj[f'{data_field}']
                w.writerow(res_dict)
        res_dict = res_dict.fromkeys(res_dict, '{}')
        
       
