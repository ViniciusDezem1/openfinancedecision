import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

#Test
#1.finish the action plan table and check the references
#2.define time zone..what is t1, t2, t3? 
#3.Before this calculation perference score. 
#4.Determine time zone: t1, t2,t3 (time is in months)
#5.All action plans in t1 to t3: Run this separtely for t1, t2, t3
#6.Check products and services for t1 to t3
#7.Write points on results yiu have generated...outcome of the analysis (Result section in th paper)

# Data for all tasks
task_names = np.array(['Automated Robo-Advisory', 'Subscription Management Services', 
                       'Bill Payment Services', 'Payment Initiation', 'Cross-Border Payments', 
                       'Cryptocurrencies', 'Peer-to-Peer Lending Platforms', 'Insurance Products',
                       'Gamification Rewards', 'Cost Management', 'Digital Engagement', 'Metaverse Interactions'])

s = np.array([1.86, 1.45, 1.36, 1.96, 1.11, 1.06, 0.96, 3.31, 1.83, 1.44, 3.25, 0.65])
t = np.array([3, 2, 1, 3, 3, 3, 3, 2, 2, 1, 1, 4]) #[3, 2, 1, 3, 3, 3, 3, 2, 2, 1, 1, 4]
I = len(s)

def pareto_optimal_tasks(s, t):
    pareto_optimal = []
    
    for i in range(I):
        dominated = False
        for j in range(I):
            if i != j:
                if t[j] <= t[i] and s[j] >= s[i]:
                    dominated = True
                    break
                
        if not dominated:
            pareto_optimal.append(i)
            
    return pareto_optimal

selected_tasks = pareto_optimal_tasks(s, t)

# Getting the Pareto optimal points and sorting them
pareto_times = t[selected_tasks]
pareto_scores = s[selected_tasks]
sorted_indices = np.argsort(pareto_times)
pareto_times = pareto_times[sorted_indices]
pareto_scores = pareto_scores[sorted_indices]

# Fitting a spline curve, adjusting spline order if necessary
spline_order = min(3, len(selected_tasks) - 1)
spline = UnivariateSpline(pareto_times, pareto_scores, k=spline_order)
t_range = np.linspace(min(pareto_times), max(pareto_times), 100)
s_fit = spline(t_range)

# Plotting
plt.figure(figsize=(6, 5))

# Shading the optimal region
plt.fill_between(t_range, s_fit, 1, color='grey', alpha=0.3, label="Optimal Region")

# Non-Pareto tasks
non_pareto = set(range(I)) - set(selected_tasks)
for idx in non_pareto:
    plt.scatter(t[idx], s[idx], color='blue')
    plt.text(t[idx], s[idx], task_names[idx], fontsize=9, ha='right')

# Pareto optimal tasks
for idx in selected_tasks:
    plt.scatter(t[idx], s[idx], color='red')
    plt.text(t[idx], s[idx], task_names[idx], fontsize=9, ha='right')

# Plotting the fitted spline curve
plt.plot(t_range, s_fit, 'g--', label='Pareto Optimal Tasks')

plt.xlabel('Minimize''\n''Time')
plt.ylabel('Maximum''\n''Preference Score')
plt.title('Action Plan for Tasks in Phase T1')
plt.legend(loc="upper right")
plt.grid(True)
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

#Test
#1.finish the action plan table and check the references
#2.define time zone..what is t1, t2, t3? 
#3.Before this calculation perference score. 
#4.Determine time zone: t1, t2,t3 (time is in months)
#5.All action plans in t1 to t3: Run this separtely for t1, t2, t3
#6.Check products and services for t1 to t3
#7.Write points on results yiu have generated...outcome of the analysis (Result section in th paper)

# Data for all tasks Product and services 
task_names = np.array(['Automated Robo-Advisory', 'Subscription Management Services', 
                       'Bill Payment Services', 'Payment Initiation', 'Cross-Border Payments', 
                       'Cryptocurrencies', 'Peer-to-Peer Lending Platforms', 'Insurance Products',
                       'Gamification Rewards', 'Cost Management', 'Digital Engagement', 'Metaverse Interactions'])

s = np.array([.40, 0.31, 0.29, 0.38, 0.22, 0.21, 0.19, 1, 0.56, 0.44, 0.83,0.17])
t = np.array([3, 2, 1, 3, 3, 3, 3, 2, 2, 1, 1, 4]) #[3, 2, 1, 3, 3, 3, 3, 2, 2, 1, 1, 4]
I = len(s)

def pareto_optimal_tasks(s, t):
    pareto_optimal = []
    
    for i in range(I):
        dominated = False
        for j in range(I):
            if i != j:
                if t[j] <= t[i] and s[j] >= s[i]:
                    dominated = True
                    break
                
        if not dominated:
            pareto_optimal.append(i)
            
    return pareto_optimal

selected_tasks = pareto_optimal_tasks(s, t)

# Getting the Pareto optimal points and sorting them
pareto_times = t[selected_tasks]
pareto_scores = s[selected_tasks]
sorted_indices = np.argsort(pareto_times)
pareto_times = pareto_times[sorted_indices]
pareto_scores = pareto_scores[sorted_indices]

# Fitting a spline curve, adjusting spline order if necessary
spline_order = min(3, len(selected_tasks) - 1)
spline = UnivariateSpline(pareto_times, pareto_scores, k=spline_order)
t_range = np.linspace(min(pareto_times), max(pareto_times), 100)
s_fit = spline(t_range)

# Plotting
plt.figure(figsize=(6, 5))

# Shading the optimal region
plt.fill_between(t_range, s_fit, 1, color='grey', alpha=0.3, label="Optimal Region")

# Non-Pareto tasks
non_pareto = set(range(I)) - set(selected_tasks)
for idx in non_pareto:
    plt.scatter(t[idx], s[idx], color='blue')
    plt.text(t[idx], s[idx], task_names[idx], fontsize=9, ha='right')

# Pareto optimal tasks
for idx in selected_tasks:
    plt.scatter(t[idx], s[idx], color='red')
    plt.text(t[idx], s[idx], task_names[idx], fontsize=9, ha='right')

# Plotting the fitted spline curve
plt.plot(t_range, s_fit, 'g--', label='Pareto Optimal Tasks')

plt.xlabel('Minimize''\n''Time')
plt.ylabel('Maximum''\n''Preference Score')
plt.title('Action Plan for Tasks in Phase T1')
plt.legend(loc="upper right")
plt.grid(True)
plt.show()



