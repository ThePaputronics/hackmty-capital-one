import React from 'react';

export const ThumbnailRecolored: React.FC = () => {
  return (
    <div
      style={{
        width: 1920,
        height: 1080,
        backgroundColor: '#f3f2f2',
        color: '#201f1d',
        fontFamily: '"Lora", Georgia, serif',
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '0 120px',
        position: 'relative',
        overflow: 'hidden',
        boxSizing: 'border-box',
      }}
    >
      {/* Background ambient lighting/glows with classical palette */}
      <div
        style={{
          position: 'absolute',
          top: -200,
          left: -150,
          width: 750,
          height: 750,
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(182, 130, 53, 0.12) 0%, transparent 70%)',
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: -200,
          right: -100,
          width: 850,
          height: 850,
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(140, 47, 57, 0.09) 0%, transparent 70%)',
          pointerEvents: 'none',
        }}
      />

      {/* Left Column: Exactly matching the reference layout */}
      <div style={{ display: 'flex', flexDirection: 'column', maxWidth: '950px', zIndex: 2 }}>
        {/* Challenge / Category Pill */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px', marginBottom: '24px' }}>
          <span
            style={{
              backgroundColor: 'rgba(182, 130, 53, 0.1)',
              border: '1.5px solid #b68235',
              borderRadius: '8px',
              padding: '8px 18px',
              color: '#7d5411',
              fontFamily: 'ui-monospace, Menlo, Consolas, monospace',
              fontSize: '15px',
              fontWeight: 700,
              letterSpacing: '2px',
              textTransform: 'uppercase',
            }}
          >
            Capital One Challenge · Real-Time Anomaly Sentinel
          </span>

          {/* Pause badge */}
          <span
            style={{
              backgroundColor: 'rgba(140, 47, 57, 0.08)',
              border: '1.5px solid #8c2f39',
              borderRadius: '6px',
              padding: '4px 10px',
              color: '#8c2f39',
              fontFamily: 'ui-monospace, Menlo, Consolas, monospace',
              fontSize: '12px',
              fontWeight: 700,
              letterSpacing: '1px',
              textTransform: 'uppercase',
            }}
          >
            PAUSE
          </span>
        </div>

        {/* Project Name */}
        <h1
          style={{
            fontSize: '110px',
            fontFamily: '"Cormorant Garamond", Georgia, serif',
            fontWeight: 700,
            letterSpacing: '6px',
            color: '#201f1d',
            margin: '0 0 16px 0',
            lineHeight: 1,
          }}
        >
          F.R.E.D
        </h1>

        {/* Subtitle / Core Hook */}
        <p
          style={{
            fontSize: '36px',
            lineHeight: 1.35,
            color: 'rgba(32, 31, 29, 0.85)',
            fontFamily: '"Cormorant Garamond", Georgia, serif',
            fontWeight: 400,
            margin: '0 0 44px 0',
          }}
        >
          Protección en tiempo real contra fraudes por manipulación antes de la liquidación SPEI.
        </p>

        {/* Highlight Stat Badges (3 cards) */}
        <div style={{ display: 'flex', gap: '20px' }}>
          {/* Card 1 */}
          <div
            style={{
              backgroundColor: '#ffffff',
              border: '1.5px solid rgba(32, 31, 29, 0.14)',
              borderRadius: '14px',
              padding: '18px 26px',
              display: 'flex',
              flexDirection: 'column',
              boxShadow: '0 4px 14px rgba(45, 41, 41, 0.05)',
            }}
          >
            <span
              style={{
                color: '#8c2f39',
                fontFamily: 'ui-monospace, Menlo, Consolas, monospace',
                fontSize: '32px',
                fontWeight: 800,
              }}
            >
              6 / 6
            </span>
            <span
              style={{
                color: 'rgba(32, 31, 29, 0.55)',
                fontFamily: '"Lora", Georgia, serif',
                fontSize: '14px',
                marginTop: '4px',
              }}
            >
              Ataques APP interceptados
            </span>
          </div>

          {/* Card 2 */}
          <div
            style={{
              backgroundColor: '#ffffff',
              border: '1.5px solid rgba(32, 31, 29, 0.14)',
              borderRadius: '14px',
              padding: '18px 26px',
              display: 'flex',
              flexDirection: 'column',
              boxShadow: '0 4px 14px rgba(45, 41, 41, 0.05)',
            }}
          >
            <span
              style={{
                color: '#2f5d4a',
                fontFamily: 'ui-monospace, Menlo, Consolas, monospace',
                fontSize: '32px',
                fontWeight: 800,
              }}
            >
              0.0%
            </span>
            <span
              style={{
                color: 'rgba(32, 31, 29, 0.55)',
                fontFamily: '"Lora", Georgia, serif',
                fontSize: '14px',
                marginTop: '4px',
              }}
            >
              Falsos positivos (PyMEs)
            </span>
          </div>

          {/* Card 3 */}
          <div
            style={{
              backgroundColor: '#ffffff',
              border: '1.5px solid rgba(32, 31, 29, 0.14)',
              borderRadius: '14px',
              padding: '18px 26px',
              display: 'flex',
              flexDirection: 'column',
              boxShadow: '0 4px 14px rgba(45, 41, 41, 0.05)',
            }}
          >
            <span
              style={{
                color: '#7d5411',
                fontFamily: 'ui-monospace, Menlo, Consolas, monospace',
                fontSize: '32px',
                fontWeight: 800,
              }}
            >
              &lt; 4 ms
            </span>
            <span
              style={{
                color: 'rgba(32, 31, 29, 0.55)',
                fontFamily: '"Lora", Georgia, serif',
                fontSize: '14px',
                marginTop: '4px',
              }}
            >
              Latencia p95 reproducible
            </span>
          </div>
        </div>
      </div>

      {/* Right Column: Visual Mockup of Mobile Active Intercept (Identical structure to reference, recolored) */}
      <div
        style={{
          transform: 'rotate(-4deg) scale(0.95)',
          filter: 'drop-shadow(0 20px 40px rgba(45, 41, 41, 0.16))',
          zIndex: 3,
        }}
      >
        <div
          style={{
            width: '380px',
            height: '660px',
            backgroundColor: '#ffffff',
            borderRadius: '40px',
            border: '4px solid #bab6b6',
            overflow: 'hidden',
            display: 'flex',
            flexDirection: 'column',
            fontFamily: '"Lora", Georgia, serif',
            position: 'relative',
          }}
        >
          {/* Dynamic Island / Notch */}
          <div
            style={{
              width: '110px',
              height: '22px',
              backgroundColor: '#eae7e7',
              margin: '12px auto 6px auto',
              borderRadius: '14px',
            }}
          />

          {/* Phone Header */}
          <div
            style={{
              padding: '10px 20px',
              borderBottom: '1px solid rgba(32, 31, 29, 0.12)',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
            }}
          >
            <span style={{ color: '#201f1d', fontWeight: 600, fontSize: '14px' }}>Banca Móvil</span>
            <span style={{ color: '#7d5411', fontSize: '12px', fontWeight: 600 }}>SPEI En Vivo</span>
          </div>

          {/* Transfer Info */}
          <div style={{ padding: '20px', flex: 1, display: 'flex', flexDirection: 'column' }}>
            <div style={{ color: 'rgba(32, 31, 29, 0.55)', fontSize: '12px', textTransform: 'uppercase' }}>
              Transferencia en curso
            </div>
            <div
              style={{
                color: '#201f1d',
                fontSize: '34px',
                fontWeight: 700,
                fontFamily: 'ui-monospace, Menlo, Consolas, monospace',
                margin: '4px 0 14px 0',
              }}
            >
              $12,450.00 <span style={{ fontSize: '14px', color: 'rgba(32, 31, 29, 0.5)' }}>MXN</span>
            </div>

            {/* Destination Container */}
            <div
              style={{
                backgroundColor: '#f3f2f2',
                padding: '10px 12px',
                borderRadius: '8px',
                marginBottom: '16px',
                border: '1px solid rgba(32, 31, 29, 0.12)',
              }}
            >
              <div style={{ fontSize: '11px', color: 'rgba(32, 31, 29, 0.55)' }}>Destinatario</div>
              <div
                style={{
                  color: '#201f1d',
                  fontSize: '12px',
                  fontFamily: 'ui-monospace, Menlo, Consolas, monospace',
                  marginTop: '2px',
                  fontWeight: 600,
                }}
              >
                646180157088992112
              </div>
              <div style={{ fontSize: '11px', color: '#7d5411', marginTop: '3px', fontWeight: 600 }}>
                STP · Beneficiario no habitual (&lt; 15 min)
              </div>
            </div>

            {/* Warning Callout Box */}
            <div
              style={{
                backgroundColor: 'rgba(140, 47, 57, 0.08)',
                border: '1.5px solid #8c2f39',
                borderRadius: '12px',
                padding: '14px',
                marginBottom: '16px',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                <span style={{ fontSize: '16px' }}>⚠️</span>
                <span style={{ color: '#8c2f39', fontWeight: 800, fontSize: '13px', letterSpacing: '0.5px' }}>
                  PAUSA POR RIESGO DE ENGAÑO
                </span>
              </div>
              <div style={{ color: '#444141', fontSize: '12px', lineHeight: 1.4 }}>
                Detectamos una llamada telefónica activa simultánea. Los bancos nunca piden transferencias por llamada.
              </div>
            </div>

            {/* Cancelled / Protected Button */}
            <div style={{ marginTop: 'auto' }}>
              <div
                style={{
                  padding: '14px',
                  backgroundColor: '#8c2f39',
                  borderRadius: '10px',
                  color: '#ffffff',
                  fontWeight: 800,
                  fontSize: '13px',
                  textAlign: 'center',
                  letterSpacing: '0.5px',
                  boxShadow: '0 4px 14px rgba(140, 47, 57, 0.3)',
                }}
              >
                ✓ $12,450.00 MXN PROTEGIDOS
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Footer bar */}
      <div
        style={{
          position: 'absolute',
          bottom: '30px',
          left: '120px',
          right: '120px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          borderTop: '1px solid rgba(32, 31, 29, 0.14)',
          paddingTop: '16px',
          color: 'rgba(32, 31, 29, 0.6)',
          fontFamily: 'ui-monospace, Menlo, Consolas, monospace',
          fontSize: '14px',
        }}
      >
        <span style={{ fontWeight: 600, color: '#7d5411' }}>sixsevencitos.tech</span>
        <span>Banco de México (SPEI) · HackMTY 2026</span>
      </div>
    </div>
  );
};
