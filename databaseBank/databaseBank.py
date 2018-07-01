# databaseBank/databaseBank.py: the databaseBank package.
#
# Copyright (C) 2018 Giuliano Jordao
#
# This file is part of databaseBank. (database part of ATM Machine System)
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

import sqlite3 

def dbConnect(dbName="banksdata.db") :
    #database connection
    dbConn = sqlite3.connect(dbName)
    return dbConn

def dbCursor(conn) : #gives the connection obj
    #creating database cursor
    dbCursor = dbConn.cursor()
    return dbCursor



def dbLoginClienteATM(cursor, banco, agencia, conta, senha) :
    _idConta = 0

    _sqlQuery = "SELECT `id_conta` FROM `contas`, `clientes_contas`, `clientes`  WHERE `contas.banco` = '%s' AND `contas.agencia` = '%s' AND `contas.conta` = '%s' AND `clientes_contas.id_conta` = `contas.id_conta` AND `clientes.id_cliente` = `clientes_contas.id_cliente` AND `clientes.senha` = '%s'" % (banco, agencia, conta, senha)

    print(_sqlQuery)

    if cursor.execute(_sqlQuery) :
        _idConta = cursor.fetchone()

        cursor.execute(




def dbPegaDadosClientePorId(idcliente) :

    return idCliente    


def dbCreateTable(cursor, tableName, fields) : #gives the cursor obj, table name and all fields u need
    #create a table
    if cursor.execute("'CREATE TABLE %s (%s)'" % tableName, fields) == True :
        return True
    else :
        return False

def dbInsertRow(cursor, tableName, values) : 
    # Insert a row of data
    if cursor.execute("INSERT INTO %s VALUES (%s)" % tableName, values) == True :
        return True
    else :
        return False

def dbCommit(connection) :
    # Save (commit) the changes
    connection.commit()

def dbClose(connection) :
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


