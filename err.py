#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *


# In[2]:


from qiskit import pulse, QuantumCircuit, schedule, transpile, execute, IBMQ
from qiskit.result import marginal_counts


# In[3]:


provider = provider = IBMQ.enable_account('c13b54ef033239c3b763d13d3426eceb2240cb81d2e828b521de45e350a87dcdd1524e8df98b022293467d66b85ee5e3292c8e20ec5bae9a164f44b5372cf8b2')


# In[4]:


backend = provider.get_backend('ibmq_armonk')


# In[5]:


qc = QuantumCircuit(1,1)
qc.measure(0, 0)


# In[6]:


job = backend.run(schedule(transpile(qc, backend), backend))


# In[7]:


k=job.result()


# In[ ]:





# In[12]:


#marginal_counts(k, indices=[0])
#marginal_counts(k, indices=[0], inplace=False, format_marginal=False)


# In[ ]:


#marginal_counts(k, indices=[0]) 


# In[ ]:




