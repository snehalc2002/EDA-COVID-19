#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




# In[10]:


df = pd.read_csv("covid_patient_dataset.csv")


# In[11]:


print(df.head())


# In[12]:


print(df.info()) 


# In[13]:


positive_cases = df[df["Test_Result"] == "Positive"]
print(positive_cases)


# In[14]:


location_counts = df["Location"].value_counts()
print(location_counts)


# In[17]:


low_oxygen = df[df["Oxygen_Level"] < 94]
print(low_oxygen)


# In[18]:


vaccinated_counts = df["Vaccinated"].value_counts()
print(vaccinated_counts)


# In[19]:


hospitalized_not_icu = df[(df["Hospitalized"] == True) & (df["ICU_Admission"] == False)]
print(hospitalized_not_icu)


# In[22]:


vaccine_counts = df["Vaccine_Type"].value_counts()
print(vaccine_counts)


# In[51]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("covid_patient_dataset.csv")


df["Age"] = pd.to_numeric(df["Age"], errors="coerce")


bins = [0, 18, 40, 60, 80, 100]
labels = ["0-18", "19-40", "41-60", "61-80", "81+"]

df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels)

age_group_icu = df[df["ICU_Admission"].isin(["Yes", True])]["Age_Group"].value_counts()


plt.figure(figsize=(8, 5))
sns.barplot(x=age_group_icu.index, y=age_group_icu.values, palette="coolwarm")
plt.xlabel("Age Group")
plt.ylabel("ICU Admissions")
plt.title("ICU Admissions by Age Group")
plt.show()


# In[26]:


import matplotlib.pyplot as plt
import seaborn as sns

# Count test results
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Test_Result", palette="coolwarm")
plt.title("COVID-19 Test Results Distribution")
plt.xlabel("Test Result")
plt.ylabel("Count")
plt.show()


# In[35]:


plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="ICU_Admission", y="Age", palette="Reds")
plt.title("ICU Admissions vs. Age")
plt.xlabel("ICU Admission")
plt.ylabel("Age")
plt.show()


# In[36]:


plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="Location", hue="Hospitalized", palette="Set2")
plt.xticks(rotation=45)
plt.title("Hospitalization Count by Location")
plt.xlabel("Location")
plt.ylabel("Count")
plt.show()


# In[39]:


plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Oxygen_Level", hue="Hospitalized", kde=False, palette="coolwarm", bins=10)
plt.title("Oxygen Levels of Hospitalized vs. Non-Hospitalized Patients")
plt.xlabel("Oxygen Level")
plt.ylabel("Frequency")
plt.show()


# In[40]:


plt.figure(figsize=(8, 5))
sns.countplot(data=df[df["Comorbidities"] != "None"], x="Comorbidities", hue="Death", palette="magma")
plt.xticks(rotation=45)
plt.title("Death Rate by Comorbidities")
plt.xlabel("Comorbidities")
plt.ylabel("Count")
plt.show()


# In[41]:


plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Vaccinated", hue="ICU_Admission", palette="viridis")
plt.title("ICU Admission vs. Vaccination Status")
plt.xlabel("Vaccinated")
plt.ylabel("Count")
plt.show()


# In[42]:


plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Symptoms", palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Distribution of Symptoms")
plt.xlabel("Symptoms")
plt.ylabel("Count")
plt.show()


# In[43]:


plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Age", y="Oxygen_Level", hue="ICU_Admission", style="ICU_Admission", palette="coolwarm", s=100)
plt.title("Age vs. Oxygen Level (ICU Admissions Highlighted)")
plt.xlabel("Age")
plt.ylabel("Oxygen Level")
plt.legend(title="ICU Admission")
plt.show()


# In[44]:


sns.pairplot(df, vars=["Age", "Oxygen_Level", "Doses_Received"], hue="ICU_Admission", palette="coolwarm", diag_kind="kde")
plt.show()


# In[47]:


plt.figure(figsize=(8, 5))
sns.lineplot(data=df.sort_values(by="Age"), x="Age", y="Oxygen_Level", marker="o", linewidth=2.5, color="blue")
plt.title("Oxygen Level Trend by Age")
plt.xlabel("Age")
plt.ylabel("Oxygen Level")
plt.show()




# In[1]:


import plotly.express as px

fig = px.scatter(df, x="Age", y="Oxygen_Level", color="ICU_Admission",
                 size="Doses_Received", hover_data=["Location", "Test_Result"],
                 title="Age vs. Oxygen Level (ICU Highlighted)")
fig.show()


# In[49]:


import matplotlib.pyplot as plt

icu_counts = df["ICU_Admission"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(icu_counts, labels=icu_counts.index, autopct="%1.1f%%", colors=["red", "blue"], startangle=90)
plt.title("ICU Admission Percentage")
plt.show()


# In[50]:


import seaborn as sns

plt.figure(figsize=(10, 5))
sns.barplot(x=df["Location"].value_counts().index, y=df["Location"].value_counts().values, palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("Location")
plt.ylabel("Number of Patients")
plt.title("Hospitalization by Location")
plt.show()


# In[ ]:




