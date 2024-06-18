from fastapi import  Request, status, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import traceback
from models.error_log_model import ErrorLog


class HTTPErrorHandler(BaseHTTPMiddleware):  
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as http_exc:
            '''error_info = {
                'error_type': 'HTTPException',
                'message': http_exc.detail,
                'traceback': '',
                'url': str(request.url),
            }
            await ErrorLog.create(**error_info)'''
            return JSONResponse(content = {'detail' : http_exc.detail},
                                status_code = http_exc.status_code)
        except Exception as e:
            error_info = {
                'type': type(e).__name__,
                'message': str(e),
                'traceback': traceback.format_exc(),
                'url': str(request.url), 
            }
            await ErrorLog.create(**error_info)
            
            content = {'detail' : f'Unhandled server error: {str(e)}'}
            return JSONResponse(content = content, status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)