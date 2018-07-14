from setuptools import setup, find_packages

def do_setup():
    setup(name='song_recognizer',
          version="0.0",
          author='upgraded-octo-discocito-2',
          description='you won't believe how many songs this song recognizer can recognize! 20 (not clickbait)',
          license='Cog*Works',
          platforms=['Windows', 'Linux', 'Mac OS-X', 'Unix'],
          packages=find_packages(),
          install_requires=['numpy>=1.12'])

if __name__ == "__main__":
    do_setup()
