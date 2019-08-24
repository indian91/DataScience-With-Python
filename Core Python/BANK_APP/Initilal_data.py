user1= {
        'name':     'Samyak',
        'bal' :      200000,
        'password':  '1234'
       }
    
user2= {
        'name':     'Chintu',
        'bal':       300000,
        'password':  '1234'
       }
    
user3= {
        'name':     'Vartika',
        'bal':       400000,
        'password':  '1234'
       }
    
user4= {
        'name':    'Chirkut',
        'bal':      500000,
        'password': '1234'
       }
    
user5= {
        'name':    'Heena',
        'bal':      600000,
        'password': '1234'
       }
    
import shelve

db  = shelve.open("database/bank.db",writeback=True)

db['1001'] = user1
db['1002'] = user2
db['1003'] = user3
db['1004'] = user4
db['1005'] = user5

db['last_acc'] = 1005

db.close()

print("Data Exported Sucessfully")
