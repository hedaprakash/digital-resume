import streamlit as st
from PIL import Image
from pathlib import Path


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "prakash_heda_cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def txt5(a, b, c):
  col1, col2, col3 = st.columns([.2,4,1.3])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Prakash Heda"
PAGE_ICON = ":wave:"
NAME = "Prakash Heda"
DESCRIPTION = """
Sr Manager - Database Reliability, Pioneer in DevOps, cloud tech and operational excellence.
"""
EMAIL = "ph@sqlfeatures.com"
Cell = "+1(408)466-8706"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/sqlfeatures",
    "LinkedIn": "https://www.linkedin.com/in/prakashheda/",
    "GitHub": "https://github.com/hedaprakash",
    "Blog": "https://sqlfeatures.com/prakashheda",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📫", Cell)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- Executive Summary ---
st.write('\n')
st.subheader("Executive Summary")
st.write(
    """
Dynamic and forward-thinking IT Executive with over a decade of leadership in database reliability engineering and cloud technology adaptation. Renowned for driving operational efficiencies and championing DevOps automation. Expert in strategic cloud migrations, data storage, backup strategies, and disaster recovery planning. Demonstrated success in enhancing system performance, achieving high uptime, and realizing significant cost reductions through cutting-edge IT solutions. Proficient in virtualization, advanced networking, and emergent cloud technologies. Committed to fostering organizational growth and technological excellence through strategic cross-functional collaboration and a dedication to continuous learning and innovation.
"""
)

# --- Areas of Expertise ---
st.write('\n')
st.subheader("Areas of Expertise")
st.info(
    """
- ✔️ Strategic Leadership & Project Management: Expert in leading cross-functional teams, managing complex database projects, and personnel management.
- ✔️ DevOps & Cloud Technologies: Skilled in automation, self-service database platforms, and strategic cloud migration.
- ✔️ Operational Excellence: Proven track record in operational support, incident management, and proactive database monitoring.
- ✔️ Infrastructure & System Performance: Proficient in cloud database management and infrastructure optimization.
- ✔️ Communication & Outreach: Effective communicator, tech speaker, and content creator.
"""
)



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
txt5("🚧", "**Sr Manager, Database Reliability | SS&C Technologies**","09/2011 - Present")
#st.write("09/2011 - Present")
st.write(
    """
- ► Led a team of 8+ FTEs across global database platforms including MSSQL, PostgreSQL, Oracle, Sybase, DB2, and MYSQL.
- ► Spearheaded a shift from legacy systems to modern database architectures, optimizing for both private and public cloud environments.
- ► Enhanced deployment speeds by 300% through the implementation of self-service cloud-based database deployments.
- ► Achieved 99.99% uptime SLA and reduced response times by 50% through advanced monitoring systems.
- ► Realized 60% cost savings by internalizing database support and improved system performance by 35% through infrastructure overhauls.
- ► Facilitated collaboration with development teams to optimize database schemas and queries, improving operational efficiency by 40%.

"""
)

# --- JOB 2
st.write('\n')
txt5("🚧", "**Sr. Database Infrastructure Administrator | Intuit Inc**","07/2008 - 09/2011")
# st.write("🚧", "**Sr. Database Infrastructure Administrator | Intuit Inc**")

#st.write("07/2008 - 09/2011")
st.write(
    """
- ► Managed on-call support services for over 200 SQL servers, including 50+ production servers.
- ► Played a key role in resource planning, database team coordination, and major projects including cloud transitions.
- ► Implemented best practices and proactive monitoring for production servers, enhancing overall database performance.
- ► Mentored DBAs and designers, focusing on performance optimization and scalable database solutions.
"""
)


# --- Technical Proficiencies ---
st.write('\n')
st.subheader("Technical Proficiencies")
st.write(
    """
- 🗄️ Database Systems: MSSQL, PostgreSQL, MongoDB
- ☁️ Cloud Platforms: AWS, Azure, VMware Private Cloud
- 🖥️ Hypervisor: VMware, PROXMOX, Hyper-V
- 👨‍💻 Programming: PowerShell, Python, SQL, Prompt Engineering
- 🛠️ DevOps Tools: Docker, Terraform, Ansible, Visual Studio Code
- 📊 Monitoring Tools: Prometheus, Grafana, Alert Manager, and Quest Spotlight
"""
)




# --- Education & Certifications ---
st.write('\n')
st.subheader("Education & Certifications")
st.write(
    """
- Graduate degree in Commerce, Ajmer University, Ajmer - India, 1995
- AWS Certified: CLF-C01: AWS Certified Cloud Practitioner
- Azure Certified: AZ-900: Microsoft Azure Fundamentals, DP-900 - Azure Data Fundamentals
- Microsoft Certified Database Administrator MCITP, MCPDBA
"""
)


# --- Additional Information ---
st.write('\n')
st.subheader("Additional Information")
st.write(
    """
- Active technology speaker and content creator.
- Regularly explore and adapt new technologies in database management and cloud platforms.
"""
)


# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")