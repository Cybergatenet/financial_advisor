// XAIRecommendationCard.jsx
import React, { useState } from 'react';
import './XAIRecommendationCard.css';

const XAIRecommendationCard = () => {
  const [showFullExplanation, setShowFullExplanation] = useState(false);

  const factors = [
    { name: 'Low P/E Ratio', impact: '+32%', positive: true, shapValue: 0.32 },
    { name: 'Positive Momentum', impact: '+28%', positive: true, shapValue: 0.28 },
    { name: 'Sector Diversification', impact: '+15%', positive: true, shapValue: 0.15 },
    { name: 'Interest Rate Sensitivity', impact: '-8%', positive: false, shapValue: -0.08 }
  ];

  return (
    <div className="xai-card">
      <div className="card-header">
        <span className="badge">⭐ AI RECOMMENDATION</span>
        <div className="title-row">
          <h2>Buy VTI</h2>
          <span className="emoji">📈</span>
        </div>
        <div className="confidence-row">
          <span className="confidence-label">Confidence: 0.89</span>
          <div className="confidence-bar">
            <div className="confidence-fill" style={{ width: '89%' }}></div>
          </div>
        </div>
      </div>

      <div className="card-body">
        <div className="section">
          <h4>🔍 TOP CONTRIBUTING FACTORS</h4>
          <div className="factors-list">
            {factors.map((factor, idx) => (
              <div key={idx} className="factor-item">
                <span>{factor.name}</span>
                <span className={factor.positive ? 'positive' : 'negative'}>
                  {factor.impact} {factor.positive ? '▲' : '▼'}
                </span>
              </div>
            ))}
          </div>
        </div>

        {showFullExplanation && (
          <div className="section">
            <h4>📊 SHAP FORCE PLOT</h4>
            {factors.map((factor, idx) => (
              <div key={idx} className="shap-row">
                <span className="shap-label">{factor.name}</span>
                <div className="shap-bar-bg">
                  <div 
                    className={`shap-bar ${factor.positive ? 'positive' : 'negative'}`}
                    style={{ width: `${Math.abs(factor.shapValue) * 100}%` }}
                  >
                    {factor.shapValue > 0 && `+${factor.shapValue.toFixed(2)}`}
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        <button 
          className="xai-button"
          onClick={() => setShowFullExplanation(!showFullExplanation)}
        >
          {showFullExplanation ? 'Hide' : 'See full SHAP explanation'} →
        </button>

        <div className="explanation-note">
          <strong>💡 Why this recommendation?</strong>
          <p>VTI offers broad market exposure with low fees. The model identified attractive valuation 
             (P/E below historical average), strong recent performance, and portfolio diversification benefits.</p>
        </div>
      </div>

      <div className="card-footer">
        ⚡ Inference time: 1.2s | Model: Random Forest (100 trees) | SHAP values calculated in real-time
      </div>
    </div>
  );
};

export default XAIRecommendationCard;