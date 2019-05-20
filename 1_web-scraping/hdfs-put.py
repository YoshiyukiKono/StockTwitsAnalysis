import subprocess
import glob

#https://community.cloudera.com/t5/CDH-Manual-Installation/amp-quot-RuntimeException-core-site-xml-not-found-amp-quot/td-p/87590
# So, I assume that the problem comes from the code where HIVE_CONF_DIR is appended to HADOOP_CONF_DIR. 
#
os.environ['HADOOP_CONF_DIR'] = "/opt/cloudera/parcels/CDH-6.1.0-1.cdh6.1.0.p0.770702/lib/spark/conf/yarn-conf"
#os.environ['HADOOP_CONF_DIR'] = "/etc/spark/conf/yarn-conf"

#args = ['hdfs', 'dfs', '-ls', '/tmp/']
HDFS_PATH_DIR = '/tmp/twits/'
args = ['hdfs', 'dfs', '-put', '', HDFS_PATH_DIR]


try:
  args_mkdir = ['hdfs', 'dfs', '-mkdir', HDFS_PATH_DIR]
  proc = subprocess.run(args_mkdir,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
  
except:
  import traceback
  traceback.print_exc()
  print("Error.")


file_list = glob.glob("./data/*")

for file in file_list:
  try:
    #res = subprocess.check_call(args)
    args[3] = file
    print(args)
    #subprocess.call(["hadoop", "fs", "-ls"])
    proc = subprocess.run(args,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    print(proc.stdout.decode("utf8"))
    
    #path = FILE_PATH + symbol + ".json"
    
    #with open(path, mode='w') as f:
    #  f.write(proc.stdout.decode("utf8"))
  
  except:
    import traceback
    traceback.print_exc()
    print("Error.")
