import redis, worker, ast
from hotqueue import HotQueue
from datahandler import datahandler

q = HotQueue("queue", host='172.17.0.1', port=6379, db=0)
rd = redis.StrictRedis(host='172.17.0.1', port=6379, db=1)
out = redis.StrictRedis(host='172.17.0.1', port=6379, db=2)
d = datahandler()


@q.worker
def execute_job(jid):
    if(jid is not None):
        job_key = worker.generate_job_key(jid)
        commands = ["All", "Date", "Country", "City", "State", "Shape", "LAT", "LNG", "LAT-LNG"]

        __update_status(job_key, "pending")
        job_info = ast.literal_eval(rd.get(job_key))

        inp = (job_info["command"]).split("=")
        if(inp[0] not in commands):
            if(inp[0] == "ADD"):
                add_data(job_key, inp[1])
            return ("Invalid Query")
        try:
            query = d.getQuery(inp[0], inp[1])
        except:
            print ("Query Failed")
            return ("Query Failed")

        try:
            outDict = instantiate_output(jid, d.toString(query))
            out.set(job_key, str(outDict))
        except:
            print ("Failure to add output to output database")
            return ("Failure to add output to output database")

        __update_status(job_key, "completed")
        job_info = ast.literal_eval(rd.get(job_key))
        print(job_info)


def __update_status(job_key, status):
    try:
        job = rd.get(job_key)
        job_info = ast.literal_eval(job)
        job_info["status"] = status
        rd.set(job_key, str(job_info))
    except:
        return ("Invalid Request")


def __update_output(job_key, output):
    try:
        output = out.get(job_key)
        out_info = ast.literal_eval(output)
        out_info["output"] = output
        out.set(job_key, str(out_info))
    except:
        return ("Invalid Request")


def instantiate_output(jid, output):
    if type(jid) == str:
        return {'id': jid,
                'output': output,
               }
    return {'id': jid.decode('utf-8'),
            'output': output.decode('utf-8'),
           }


def add_data(job_key, data_dict):
    try:
        data_dict = ast.literal_eval(data_dict)
        __update_status(job_key, "completed")
        job_info = ast.literal_eval(rd.get(job_key))
        print(job_info)
        print(d.addData(data_dict))
    except:
        return False


execute_job()
