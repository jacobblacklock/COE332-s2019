import redis, uuid, time, datetime, ast
from hotqueue import HotQueue

q = HotQueue("queue", host='172.17.0.1', port=6379, db=0)
rd = redis.StrictRedis(host='172.17.0.1', port=6379, db=1)
out = redis.StrictRedis(host='172.17.0.1', port=6379, db=2)




def generate_jid():
    return str(uuid.uuid4())


def generate_job_key(jid):
    return 'job.{}'.format(jid)


def instantiate_job(jid, status, command, time):
    if type(jid) == str:
        return {'status': status,
                'command': command,
                'time': time,
                'id': jid,
               }
    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'command': command.decode('utf-8'),
            'time': time.decode('utf-8')
           }




def __save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd.set(job_key, str(job_dict))


def __queue_job(jid):
    """Add a jid to the redis queue"""
    q.put(jid)


def add_job(command, status="submitted"):
    """Add an entire job to the redis database"""
    time = datetime.datetime.now()
    jid = generate_jid()
    job_key = generate_job_key(jid)
    job_dict = instantiate_job(jid, status, command, str(time))
    __save_job(job_key, job_dict)
    __queue_job(jid)
    return job_key




def __save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd.set(job_key, str(job_dict))





def get_status(job_key):
    try:
        job = ast.literal_eval(rd.get(job_key))
        if(rd.get(job_key) == None):
            rd.set(job_key, str(job))
        return job["status"]
    except:
        return ("Invalid Request")



def get_output(job_key):
    if("completed" not in get_status(job_key)):
        return ("The job has not been completed yet")
    try:
        redisOut = out.get(job_key)
        out_info = ast.literal_eval(redisOut)
        return out_info["output"]
    except:
        return ("Invalid Request")

def add_data(data_dict):
    try:
        jid = generate_jid()
        job_key = generate_job_key(jid)
        job_dict = {'command': "ADD=" + str(data_dict)}
        __save_job(job_key, job_dict)
        __queue_job(jid)
        return (job_key)
    except:
        return ("Failed to Add")


#Debugging and Testing

#key = "job.06fc0bef-c404-46c0-b1aa-14f4bcaf2014"
#key = add_job("Date="+start+"-"+end)
#print (get_status(key))
#print(get_output(key))
