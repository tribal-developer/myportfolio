from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200) # e.g., Cyber Security Analyst
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=[('Network', 'Network'), ('Security', 'Security'), ('Dev', 'Development')])
    icon_class = models.CharField(max_length=50, help_text="FontAwesome class, e.g., fa-brands fa-python")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    tech_stack = models.CharField(max_length=200) # e.g., Django, React, Nmap
    link = models.URLField()
    github_link = models.URLField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) # Null means Present
    description = models.TextField()
    from_link = models.CharField(max_length=100, default="")
    about_company = models.URLField(blank=True)

    def __str__(self):
        return f"{self.role} at {self.company}"

class Certification(models.Model):
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    date_obtained = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
