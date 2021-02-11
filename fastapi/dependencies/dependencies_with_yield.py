from fastapi import Depends


# dependencies that do extra steps after finishing
# - yield a single time
# - requires python 3.7+
# - requires async-exit, async-generator

# Examples
# - yield is what is injected into path operations and other dependencies
# - statements after yield are executed after the response has been delivered
#
# async def get_db():
#     db = DBSession()
#     try:
#         yield db
#     finally::
#         db.close()

# Dependencies with yield
# - Exceptions cannot be caught after a yield because the response has already been sent
# - try/catch before the yield
# - try/catch to clean up after a response is sent
# - fastapi will internally convert it to a content manager and combine it with other related tools
#
# async  def dependency_a():
#     dep_a = generate_dep_a()
#     try:
#         yield dep_a
#
#     finally:
#         dep_a.close()
#
#
# async def dependency_b(dep_a=Depends(dependency_a)):
#     dep_b = generate_dep_b()
#     try:
#         yield dep_b
#
#     finally:
#         dep_b(dep_a)
#
#
# async def dependency_c(dep_b=Depends(dependency_b)):
#     dep_c = generate_dep_c()
#     try:
#         yield dep_c
#
#     finally:
#         dep_c.close(deb_b)


# Dependencies with Context Managers
#
# class MySuperContextManager:
#     def __init__(self):
#         self.db = DBSession()
#
#     def __enter__(self):
#         return self.db
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.db.close()


# async def get_db():
#     with MySuperContextManager() ad db:
#         yield get_db
