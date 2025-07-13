import sqlite3


def insertUsuDB(login, senha):
    conn, mysql_link = abrirConexao()

    sql = "INSERT INTO usu (LOGIN, SENHA) VALUES (?,?);"
    val = (login, senha)
    mysql_link.execute(sql, val )

    fecharConexao(conn)

    return mysql_link.rowcount


def selectUsuDB():
    conn, mysql_link = abrirConexao()

    sql = "SELECT USU_ID,LOGIN FROM usu;"
    mysql_link.execute(sql, )
    result = mysql_link.fetchall()

    fecharConexao(conn)

    return result


def selectDesDB(login):
    conn, mysql_link = abrirConexao()

    sql = "SELECT USU_ID FROM usu WHERE LOGIN=?;"
    val = (login,)
    mysql_link.execute(sql, val )
    result = mysql_link.fetchall()

    fecharConexao(conn)

    return result


def insertMenDB(idr, idd, men, hor):
    conn, mysql_link = abrirConexao()

    sql = "INSERT INTO men (MEN_REM_ID, MEN_DES_ID, MENS, HOR) VALUES (?,?,?,?);"
    val = (idr, idd, men, hor)
    mysql_link.execute(sql, val )

    fecharConexao(conn)

    return mysql_link.rowcount


def selectMenDB(idr, idd):
    conn, mysql_link = abrirConexao()

    sql = "SELECT MENS,LOGIN FROM men,usu WHERE (MEN_REM_ID =?  OR MEN_DES_ID = ? AND MEN_REM_ID = ?  OR MEN_DES_ID = ?) AND MEN_REM_ID=USU_ID ORDER BY HOR ASC;"
    val = (idr, idr, idd, idd)
    mysql_link.execute(sql, val )
    result = mysql_link.fetchall()

    fecharConexao(conn)

    return result


def selectloginDB(login, senha):
    conn, mysql_link = abrirConexao()

    sql = "SELECT USU_ID,LOGIN FROM usu WHERE  LOGIN=? and SENHA=?;"
    val = (login, senha)
    mysql_link.execute(sql, val )
    result = mysql_link.fetchall()

    fecharConexao(conn)

    return result


def abrirConexao():
    try:
        conn = sqlite3.connect('MENSA.db')
        mysql_link = conn.cursor()
        return conn, mysql_link
    except sqlite3.Error as e:
        print "Erro ao conectar ao banco de dados:", e
        return None, None


def fecharConexao(conn):
    if conn:
        conn.commit()  # Salva mudancas
        conn.close()
