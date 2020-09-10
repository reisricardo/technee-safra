import datetime

class user:

    def check_user_register(self, conn, cursor):
        if hasattr(self, 'identification'):
            
            sql = '''
                SELECT * FROM `open`.`users` WHERE `uid` = %(uid)s;
            '''
            val = {
                "uid" : self.uid
            }
            cursor.execute(sql, val) 
            data = cursor.fetchall()
                
            records_number = cursor.rowcount
            

            if records_number <= 0:
                return False, self
            else:
               
                for row in data:
                    self.name = row['name'],
                    self.creation_date = row['creation_date'].isoformat(),
                    self.temporary_token = row['temporary_token'],
                    self.creation_temporary_token = row['creation_temporary_token'],
                    self.failed_attempts = row['failed_attempts'],
                    self.blocked_account = row['blocked_account']
                    return True, self
        else:
            raise ValueError('The user object does not have the "CPF" attributeF')
            return False, self
            