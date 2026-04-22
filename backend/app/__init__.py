# cd financial_advisor

# # Create __init__.py files
# touch backend/__init__.py
# touch backend/app/__init__.py

# # Create frontend files
# cat > frontend/src/index.js << 'EOF'
# import React from 'react';
# import ReactDOM from 'react-dom/client';
# import App from './App';

# const root = ReactDOM.createRoot(document.getElementById('root'));
# root.render(
#   <React.StrictMode>
#     <App />
#   </React.StrictMode>
# );
# EOF

# cat > frontend/public/index.html << 'EOF'
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="utf-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1" />
#     <title>AI Financial Advisor</title>
# </head>
# <body>
#     <div id="root"></div>
# </body>
# </html>
# EOF

# echo "All files created successfully!"

