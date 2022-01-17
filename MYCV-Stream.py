#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO
#%matplotlib inline


# In[5]:


Header = '>>>This resume was generated entirely in Python. For full sourcecode, view my portfolio.'
#Name and profession
st.title('Resume - Created by Omid Ghamiloo')
st.markdown("This Resume is created by Matplotlib and Streamlit by Python in just three hours. Definitely It's possible to make it very complete. In the near future, I will work on it more. Now you can change everything from sidebar and by pressing Enter, you can see the change in the CV. You can't download it, because it's just a sample of my coding in data visualization and web app. For downloading my CV, please go to my website - www.ghamiloo.info. Thank you so much.")

Name = st.sidebar.text_input("name and surename", 'Omid Ghamiloo')
Title = st.sidebar.text_input("your job", 'Data Science & Analytics')
#Contact
st.sidebar.markdown('Contact detail')
City = st.sidebar.text_input("city", 'Rome, Italy')
City = 'Address: '+City
Phone = st.sidebar.text_input("phone", '+393891249525')
Phone = 'Phone: '+Phone
Email = st.sidebar.text_input("email", 'omid.ghamiloo@gmail.com')
Email = 'Email: '+Email
Linkedin = st.sidebar.text_input("linkedin", '/in/omid-ghamiloo/')
Linkedin = 'Linkedin: '+Linkedin
Github = st.sidebar.text_input("github", 'github.com/omidgh1')
Github = 'Github: '+Github
Website = st.sidebar.text_input("website", 'ghamiloo.info')
Website = 'Website: ' + Website
About_text = 'I’m hard work and trying to improve my career through the given tasks.\n'+        'I may not know everything but I believe that you can google the solutions\n'+        'for all problems, but you need to know how to do it and my experiences can\n'+        'prove it. So, I try to do my best to learn and foster myself to grow in my\n'+        'position. I just need to love it. All the skills which are in this CV are my\n'+        'position. I also give credit to teamwork, so I try to be the best on that.\n'+        'You can find my data. analysis and web scraping projects on my github.'
About = st.sidebar.text_input("About", About_text)


# In[6]:


#Work
WorkHeader = 'EXPERIENCE'
st.sidebar.markdown('First EXPERIENCE')
WorkOneTitle = st.sidebar.text_input('First Work Title','Dirac s.r.l / Data Scientist')
WorkOneTime = st.sidebar.text_input('First Work date','July 2021 - Present')
Descone_1 = st.sidebar.text_input('First work, First Responsibility','Air pollution analysis and modelling')
Descone_2 =  st.sidebar.text_input('First work, Second Responsibility',
                           'Air pollution mapping in high resolution scale by python and Arcgis')
Descone_3 =  st.sidebar.text_input('First work, Third Responsibility','Web Scraping for marketing')
Descone_4 =  st.sidebar.text_input('First work, Fourth Responsibility','Facebook digital marketing')
Descone_5 = st.sidebar.text_input('First work,Fifth Responsibility','Competitors analysis')
Descone_6 = st.sidebar.text_input('First work,Sixth Responsibility','AWS cloud')
WorkoneDesc = Descone_1+'\n'+Descone_2+'\n'+Descone_3+'\n'+Descone_4+'\n'+Descone_5+'\n'+Descone_6
st.sidebar.markdown('Second EXPERIENCE')
WorkTwoTitle = st.sidebar.text_input('Second Work Title','Piersez / IT Administrator and Data Analyst')
WorkTwoTime = st.sidebar.text_input('Second Work date','2016 - 2018')
Desctwo_1 = st.sidebar.text_input('Second work, First Responsibility',
                          'Microsoft Server installation and configuration')
Desctwo_2 =  st.sidebar.text_input('Second work, Second Responsibility',
                           'Microsoft CRM Server base installation and configuration')
Desctwo_3 =  st.sidebar.text_input('Second work, Third Responsibility','website develop')
Desctwo_4 =  st.sidebar.text_input('Second work, Fourth Responsibility','Sale process analysis')
Desctwo_5 = st.sidebar.text_input('Second work,Fifth Responsibility','Sale analysis')
WorktwoDesc = Desctwo_1+'\n'+Desctwo_2+'\n'+Desctwo_3+'\n'+Desctwo_4+'\n'+Desctwo_5
st.sidebar.markdown('Third EXPERIENCE')
WorkThreeTitle = st.sidebar.text_input('Third Work Title','Otolux / IT Administratior')
WorkThreeTime = st.sidebar.text_input('Third Work date','2012 - 2015')
Descthree_1 = st.sidebar.text_input('Third work, First Responsibility',
                          'Network developer and redesign the network layers')
Descthree_2 =  st.sidebar.text_input('Third work, Second Responsibility',
                           'website develop')
WorkthreeDesc = Descthree_1+'\n'+Descthree_2


# In[7]:


#Education
EDUHeader = 'EDUCATION'
st.sidebar.markdown('First EDUCATION')
MasterUni_name = st.sidebar.text_input('Master University Name','Sapienza University')
MasterUni_field = st.sidebar.text_input('Master Field','Master of Data Science')
MasterUni = MasterUni_field +' - '+MasterUni_name
MasterUni_date = st.sidebar.text_input('Master Course Date','2018 - Present')
MasterUni_city = st.sidebar.text_input('Master University Location','Rome, Italy')
MasterUni_thesis = st.sidebar.text_input('Master Thesis','Thesis: Air pollution mapping in high resolution scale')
st.sidebar.markdown('Second EDUCATION')
BachelorUni_name = st.sidebar.text_input('Bachelor University Name','Eyvanakey University')
BachelorUni_field = st.sidebar.text_input('Bachelor Field','Bachelor of Information Technology')
BachelorUni = BachelorUni_field +' - '+BachelorUni_name
BachelorUni_date = st.sidebar.text_input('Bachelor Course Date','2010 - 2014')
BachelorUni_city = st.sidebar.text_input('Bachelor University Location','Tehran, Iran')
BachelorUni_thesis = st.sidebar.text_input('Bachelor Thesis','Thesis: Cloud computing in applications')


# In[8]:


#Skills
SkillsH = 'Skills'
st.sidebar.markdown('First Skill')
Skill_1 = st.sidebar.text_input('First Skill','Python')
Skill_10 = st.sidebar.text_input('First Skill_First SubSkill','- Main Tools')
Skill_10_1 = st.sidebar.text_input('First Skill_First SubsubSkill','> Pandas')
Skill_10_2 = st.sidebar.text_input('First Skill_Second SubsubSkill','> Numpy')
Skill_11 = st.sidebar.text_input('First Skill_Second SubSkill','- Data Mining')
Skill_11_1 = st.sidebar.text_input('First Skill_First SubsubSkill','> Beautiful Soup')
Skill_11_2 = st.sidebar.text_input('First Skill_Second SubsubSkill','> Selenium')
Skill_12 = st.sidebar.text_input('First Skill_Third SubSkill','- Machine Learning')
Skill_12_1 = st.sidebar.text_input('First Skill_First SubsubSkill','> Scikit-learn')
Skill_12_2 = st.sidebar.text_input('First Skill_Second SubsubSkill','> TensorFlow')
Skill_13 = st.sidebar.text_input('First Skill_Fourth SubSkill','- Data Visualization')
Skill_13_1 = st.sidebar.text_input('First Skill_First SubsubSkill','> Mathplotlib')
Skill_13_2 = st.sidebar.text_input('First Skill_Se SubsubSkill','> Seaborn')
Skill_14 = st.sidebar.text_input('First Skill_Fifth SubSkill','- Web App')
Skill_14_1 = st.sidebar.text_input('First Skill_First SubsubSkill','> Streamlit')
st.sidebar.markdown('Second Skill')
Skill_2 = st.sidebar.text_input('Second Skill','IT Networking')
Skill_20 = st.sidebar.text_input('Second Skill_First SubSkill','- Microsoft Server')
Skill_20_1 = st.sidebar.text_input('Second Skill_First SubsubSkill','> AD DS')
Skill_20_2 = st.sidebar.text_input('Second Skill_First SubsubSkill','> Group Policy')
Skill_20_3 = st.sidebar.text_input('Second Skill_First SubsubSkill','> Hyper_v')
Skill_20_4 = st.sidebar.text_input('Second Skill_First SubsubSkill','> Storage Solution')
Skill_21 = st.sidebar.text_input('Second Skill_Second SubSkill','- Vmware ESXi')
Skill_22 = st.sidebar.text_input('Second Skill_Third SubSkill','- Veeam Backup')
Skill_23 = st.sidebar.text_input('Second Skill_Fourth SubSkill','- Cisco Route and Switch')
Skill_24 = st.sidebar.text_input('Second Skill_Fifth SubSkill','- Microsoft CRM')
Skill_25 = st.sidebar.text_input('Second Skill_Sixth SubSkill','- Amazon AWS')


# In[9]:


fig, ax = plt.subplots(figsize=(10, 12.7))
# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.75, xmin=0, xmax=1, color='#ffffff', linewidth=3)
# set background color
ax.set_facecolor('white')
# remove axes
plt.axis('off')
# Name
plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.75)
plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)

plt.annotate(About, (.02,.767), weight='regular', fontsize=10)

#Contact
plt.annotate(Email, (.73,.95), weight='regular', fontsize=8.5, color='#ffffff')
plt.annotate(City, (.73,.927), weight='regular', fontsize=9, color='#ffffff')
plt.annotate(Phone, (.73,.904), weight='regular', fontsize=9, color='#ffffff')
plt.annotate(Linkedin, (.73,.881), weight='regular', fontsize=9, color='#ffffff')
plt.annotate(Github, (.73,.858), weight='regular', fontsize=9, color='#ffffff')
plt.annotate(Website, (.73,.835), weight='regular', fontsize=9, color='#ffffff')

y = 0.72
space = 0.023
#Work Experience
plt.annotate(WorkHeader, (.02,y), weight='bold', fontsize=12, color='#58C1B2')
y = y-(space+0.015)
plt.annotate(WorkOneTitle, (.02,y), weight='bold', fontsize=12)
y = y-space
plt.annotate(WorkOneTime, (.02,y), weight='regular', fontsize=10)
y = y-(space+(4*0.023))
plt.annotate(WorkoneDesc, (.04,y), weight='regular', fontsize=10)
y = y-(space+0.015)
plt.annotate(WorkTwoTitle, (.02,y), weight='bold', fontsize=12)
y = y-space
plt.annotate(WorkTwoTime, (.02,y), weight='regular', fontsize=10)
y = y-(space+(3.3*0.023))
plt.annotate(WorktwoDesc, (.04,y), weight='regular', fontsize=10)
y = y-(space+0.015)
plt.annotate(WorkThreeTitle, (.02,y), weight='bold', fontsize=12)
y = y-space
plt.annotate(WorkThreeTime, (.02,y), weight='regular', fontsize=10)
y = y-(space+(0.75*0.023))
plt.annotate(WorkthreeDesc, (.04,y), weight='regular', fontsize=10)

#Education
y = y-(space+0.02)
plt.annotate(EDUHeader, (.02,y), weight='bold', fontsize=12, color='#58C1B2')
y = y-(space+0.015)
plt.annotate(MasterUni, (.02,y), weight='bold', fontsize=11.5)
y = y-space
plt.annotate(MasterUni_date, (.04,y), weight='regular', fontsize=10)
y = y-space
plt.annotate(MasterUni_city, (.04,y), weight='regular', fontsize=10)
y = y-space
plt.annotate(MasterUni_thesis, (.04,y), weight='regular', fontsize=11)
y = y-(space+0.015)
plt.annotate(BachelorUni, (.02,y), weight='bold', fontsize=11.5)
y = y-space
plt.annotate(BachelorUni_date, (.04,y), weight='regular', fontsize=10)
y = y-space
plt.annotate(BachelorUni_city, (.04,y), weight='regular', fontsize=10)
y = y-space
plt.annotate(BachelorUni_thesis, (.04,y), weight='regular', fontsize=11)

y = 0.72
space = 0.023
#Skills
plt.annotate(SkillsH, (.73,y), weight='bold', fontsize=12, color='#ffffff')
y = y-(space+0.015)
plt.annotate(Skill_1, (.73,y), weight='regular', fontsize=12, color='#ffffff')
y = y-space
plt.annotate(Skill_10, (.74,y), weight='regular', fontsize=11, color='#ffffff')
y = y-space
plt.annotate(Skill_10_1, (.76,y), weight='regular', fontsize=10, color='#ffffff')
y = y-space
plt.annotate(Skill_10_2, (.76,y), weight='regular', fontsize=10, color='#ffffff')

y = y-(space+0.01)
plt.annotate(Skill_11, (.74,y), weight='regular', fontsize=11, color='#ffffff')
y = y-space
plt.annotate(Skill_11_1, (.76,y), weight='regular', fontsize=10, color='#ffffff')
y = y-space
plt.annotate(Skill_11_2, (.76,y), weight='regular', fontsize=10, color='#ffffff')

y = y-(space+0.01)
plt.annotate(Skill_12, (.74,y), weight='regular', fontsize=11, color='#ffffff')
y = y-space
plt.annotate(Skill_12_1, (.76,y), weight='regular', fontsize=10, color='#ffffff')
y = y-space
plt.annotate(Skill_12_2, (.76,y), weight='regular', fontsize=10, color='#ffffff')

y = y-(space+0.01)
plt.annotate(Skill_13, (.74,y), weight='regular', fontsize=11, color='#ffffff')
y = y-space
plt.annotate(Skill_13_1, (.76,y), weight='regular', fontsize=10, color='#ffffff')
y = y-space
plt.annotate(Skill_13_2, (.76,y), weight='regular', fontsize=10, color='#ffffff')

y = y-(space+0.01)
plt.annotate(Skill_14, (.74,y), weight='regular', fontsize=11, color='#ffffff')
y = y-space
plt.annotate(Skill_14_1, (.76,y), weight='regular', fontsize=10, color='#ffffff')

y = y-(space+0.015)
plt.annotate(Skill_2, (.73,y), weight='regular', fontsize=12, color='#ffffff')
y = y-space
plt.annotate(Skill_20, (.74,y), weight='regular', fontsize=11, color='#ffffff')
y = y-space
plt.annotate(Skill_20_1, (.76,y), weight='regular', fontsize=10, color='#ffffff')
y = y-space
plt.annotate(Skill_20_2, (.76,y), weight='regular', fontsize=10, color='#ffffff')
y = y-space
plt.annotate(Skill_20_3, (.76,y), weight='regular', fontsize=10, color='#ffffff')
y = y-space
plt.annotate(Skill_20_4, (.76,y), weight='regular', fontsize=10, color='#ffffff')
y = y-space
plt.annotate(Skill_21, (.74,y), weight='regular', fontsize=11, color='#ffffff')
y = y-space
plt.annotate(Skill_22, (.74,y), weight='regular', fontsize=11, color='#ffffff')
y = y-space
plt.annotate(Skill_23, (.74,y), weight='regular', fontsize=11, color='#ffffff')
y = y-space
plt.annotate(Skill_24, (.74,y), weight='regular', fontsize=11, color='#ffffff')
y = y-space
plt.annotate(Skill_25, (.74,y), weight='regular', fontsize=11, color='#ffffff')

st.pyplot(fig)


# In[ ]:




