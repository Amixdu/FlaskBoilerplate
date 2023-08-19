from flask import request, jsonify
from firebase_admin import auth
from functools import wraps

def verify_token(func):
  @wraps(func)
  def decorated_function(*args, **kwargs):
      token = request.headers.get('Authorization')
      if not token:
          return jsonify({'error': 'Unauthorized'}), 401
      try:
          # Verify the ID token
          decoded_token = auth.verify_id_token(token)

          # Call the original function with the verified user information
          return func(*args, authenticated_user=decoded_token, **kwargs)

      except auth.InvalidIdTokenError:
          return jsonify({'error': 'Invalid token'}), 401

  return decorated_function