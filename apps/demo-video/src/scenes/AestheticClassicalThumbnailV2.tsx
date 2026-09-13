import React from 'react';

export const AestheticClassicalThumbnailV2: React.FC = () => {
  return (
    <div
      style={{
        width: 1920,
        height: 1080,
        backgroundColor: '#f3f2f2',
        color: '#201f1d',
        fontFamily: '"Lora", Georgia, serif',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        padding: '70px 90px 50px 90px',
        boxSizing: 'border-box',
        position: 'relative',
        overflow: 'hidden',
      }}
    >
      {/* Editorial Decorative Background Washes */}
      <div
        style={{
          position: 'absolute',
          top: -200,
          right: 350,
          width: 850,
          height: 850,
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(182, 130, 53, 0.09) 0%, transparent 68%)',
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: -180,
          right: -60,
          width: 800,
          height: 800,
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(140, 47, 57, 0.08) 0%, transparent 68%)',
          pointerEvents: 'none',
        }}
      />

      {/* Top Header */}
      <header
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          borderBottom: '1px solid rgba(32, 31, 29, 0.14)',
          paddingBottom: '22px',
          zIndex: 2,
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
          <span
            style={{
              fontSize: '12px',
              letterSpacing: '0.22em',
              textTransform: 'uppercase',
              color: '#b68235',
              fontWeight: 600,
            }}
          >
            Capital One Challenge · HackMTY 2026
          </span>
          <span style={{ color: 'rgba(32, 31, 29, 0.25)' }}>|</span>
          <span
            style={{
              fontSize: '12px',
              letterSpacing: '0.14em',
              textTransform: 'uppercase',
              color: 'rgba(32, 31, 29, 0.65)',
            }}
          >
            Real-Time Anomaly Sentinel
          </span>
        </div>

        {/* Live Pill Badge */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            padding: '7px 16px',
            border: '1px solid rgba(32, 31, 29, 0.16)',
            borderRadius: '100px',
            backgroundColor: '#ffffff',
            boxShadow: '0 2px 4px rgba(45, 43, 43, 0.05)',
          }}
        >
          <span
            style={{
              width: '8px',
              height: '8px',
              borderRadius: '50%',
              backgroundColor: '#8c2f39',
              boxShadow: '0 0 0 3px rgba(140, 47, 57, 0.18)',
            }}
          />
          <span
            style={{
              fontSize: '12px',
              letterSpacing: '0.1em',
              textTransform: 'uppercase',
              fontFamily: 'monospace',
              color: '#201f1d',
              fontWeight: 700,
            }}
          >
            sixsevencitos.tech
          </span>
        </div>
      </header>

      {/* Hero Layout: Left Content + Right Phone Mockup */}
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: '1.2fr 0.8fr',
          gap: '60px',
          alignItems: 'center',
          flex: 1,
          padding: '10px 0',
          zIndex: 2,
        }}
      >
        {/* Left Column */}
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          {/* Category kicker */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '14px' }}>
            <span
              style={{
                fontSize: '11px',
                letterSpacing: '0.15em',
                textTransform: 'uppercase',
                padding: '4px 10px',
                border: '1px solid #8c2f39',
                color: '#8c2f39',
                backgroundColor: 'rgba(140, 47, 57, 0.06)',
                borderRadius: '3px',
                fontWeight: 700,
                fontFamily: 'monospace',
              }}
            >
              PAUSE · Pre-Settlement Guard
            </span>
            <span
              style={{
                fontSize: '11.5px',
                letterSpacing: '0.12em',
                textTransform: 'uppercase',
                color: '#7d5411',
                fontWeight: 600,
              }}
            >
              SPEI 24/7 México
            </span>
          </div>

          {/* Hero Title */}
          <h1
            style={{
              fontFamily: '"Cormorant Garamond", Georgia, serif',
              fontSize: '125px',
              fontWeight: 600,
              letterSpacing: '-0.02em',
              lineHeight: 0.9,
              margin: '0 0 20px 0',
              color: '#201f1d',
            }}
          >
            F.R.E.D
          </h1>

          {/* Value Prop Hook */}
          <p
            style={{
              fontSize: '34px',
              fontFamily: '"Cormorant Garamond", Georgia, serif',
              fontStyle: 'italic',
              lineHeight: 1.25,
              color: 'rgba(32, 31, 29, 0.88)',
              margin: '0 0 34px 0',
              maxWidth: '32ch',
            }}
          >
            Intervenir antes del envío, porque después ya no hay promesa posible.
          </p>

          {/* 3 Metrics Cards */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '16px', maxWidth: '820px' }}>
            <div
              style={{
                backgroundColor: '#ffffff',
                border: '1px solid rgba(32, 31, 29, 0.14)',
                borderRadius: '6px',
                padding: '18px 22px',
                boxShadow: '0 2px 6px rgba(45, 43, 43, 0.04)',
                borderTop: '3.5px solid #8c2f39',
              }}
            >
              <div
                style={{
                  fontSize: '11px',
                  letterSpacing: '0.12em',
                  textTransform: 'uppercase',
                  color: 'rgba(32, 31, 29, 0.55)',
                  marginBottom: '6px',
                  fontWeight: 600,
                }}
              >
                APP Interceptados
              </div>
              <div
                style={{
                  fontFamily: '"Cormorant Garamond", Georgia, serif',
                  fontSize: '46px',
                  lineHeight: 1,
                  fontWeight: 600,
                  color: '#8c2f39',
                }}
              >
                6 / 6
              </div>
              <div style={{ fontSize: '12px', color: 'rgba(32, 31, 29, 0.65)', marginTop: '4px' }}>
                100% recall en coerción
              </div>
            </div>

            <div
              style={{
                backgroundColor: '#ffffff',
                border: '1px solid rgba(32, 31, 29, 0.14)',
                borderRadius: '6px',
                padding: '18px 22px',
                boxShadow: '0 2px 6px rgba(45, 43, 43, 0.04)',
                borderTop: '3.5px solid #2f5d4a',
              }}
            >
              <div
                style={{
                  fontSize: '11px',
                  letterSpacing: '0.12em',
                  textTransform: 'uppercase',
                  color: 'rgba(32, 31, 29, 0.55)',
                  marginBottom: '6px',
                  fontWeight: 600,
                }}
              >
                Falsos Positivos
              </div>
              <div
                style={{
                  fontFamily: '"Cormorant Garamond", Georgia, serif',
                  fontSize: '46px',
                  lineHeight: 1,
                  fontWeight: 600,
                  color: '#2f5d4a',
                }}
              >
                0.0<span style={{ fontSize: '20px', fontFamily: '"Lora", serif' }}>%</span>
              </div>
              <div style={{ fontSize: '12px', color: 'rgba(32, 31, 29, 0.65)', marginTop: '4px' }}>
                426 transacciones PyME
              </div>
            </div>

            <div
              style={{
                backgroundColor: '#ffffff',
                border: '1px solid rgba(32, 31, 29, 0.14)',
                borderRadius: '6px',
                padding: '18px 22px',
                boxShadow: '0 2px 6px rgba(45, 43, 43, 0.04)',
                borderTop: '3.5px solid #b68235',
              }}
            >
              <div
                style={{
                  fontSize: '11px',
                  letterSpacing: '0.12em',
                  textTransform: 'uppercase',
                  color: 'rgba(32, 31, 29, 0.55)',
                  marginBottom: '6px',
                  fontWeight: 600,
                }}
              >
                Latencia P95
              </div>
              <div
                style={{
                  fontFamily: '"Cormorant Garamond", Georgia, serif',
                  fontSize: '46px',
                  lineHeight: 1,
                  fontWeight: 600,
                  color: '#201f1d',
                }}
              >
                3.6<span style={{ fontSize: '18px', fontFamily: '"Lora", serif', color: 'rgba(32, 31, 29, 0.6)' }}> ms</span>
              </div>
              <div style={{ fontSize: '12px', color: 'rgba(32, 31, 29, 0.65)', marginTop: '4px' }}>
                Decisión en tiempo real
              </div>
            </div>
          </div>
        </div>

        {/* Right Column: Hero Floating Phone Mockup */}
        <div
          style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            position: 'relative',
          }}
        >
          {/* Classical Frame with Soft Ambient Shadow */}
          <div
            style={{
              width: '420px',
              backgroundColor: '#eae9e9',
              border: '1px solid #bab6b6',
              borderRadius: '32px',
              padding: '14px',
              boxShadow: '0 28px 70px rgba(45, 41, 41, 0.18), 0 6px 16px rgba(45, 41, 41, 0.08)',
              transform: 'rotate(-2.5deg)',
            }}
          >
            <div
              style={{
                backgroundColor: '#f3f2f2',
                border: '1px solid rgba(32, 31, 29, 0.14)',
                borderRadius: '24px',
                overflow: 'hidden',
                boxShadow: 'inset 0 1px 3px rgba(0, 0, 0, 0.03)',
              }}
            >
              {/* Phone App Bar */}
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  padding: '14px 20px',
                  borderBottom: '1px solid rgba(32, 31, 29, 0.14)',
                  fontSize: '11px',
                  letterSpacing: '0.14em',
                  textTransform: 'uppercase',
                  fontWeight: 600,
                  color: 'rgba(32, 31, 29, 0.7)',
                }}
              >
                <span>Banca Móvil</span>
                <span style={{ color: '#b68235', fontWeight: 700 }}>SPEI</span>
              </div>

              {/* Phone Body */}
              <div style={{ padding: '24px 22px', display: 'flex', flexDirection: 'column', gap: '18px' }}>
                <div>
                  <div
                    style={{
                      fontSize: '11px',
                      letterSpacing: '0.12em',
                      textTransform: 'uppercase',
                      color: 'rgba(32, 31, 29, 0.55)',
                    }}
                  >
                    Transferencia propuesta
                  </div>
                  <div
                    style={{
                      fontFamily: '"Cormorant Garamond", Georgia, serif',
                      fontSize: '44px',
                      fontWeight: 600,
                      marginTop: '4px',
                      color: '#201f1d',
                      lineHeight: 1,
                    }}
                  >
                    $12,450.00{' '}
                    <span style={{ fontSize: '16px', fontFamily: '"Lora", serif', color: 'rgba(32, 31, 29, 0.5)' }}>
                      MXN
                    </span>
                  </div>
                </div>

                {/* Recipient Details */}
                <div
                  style={{
                    backgroundColor: '#ffffff',
                    border: '1px solid rgba(32, 31, 29, 0.12)',
                    borderRadius: '8px',
                    padding: '14px 16px',
                  }}
                >
                  <div style={{ fontSize: '11px', color: 'rgba(32, 31, 29, 0.55)', textTransform: 'uppercase' }}>
                    Beneficiario
                  </div>
                  <div style={{ fontFamily: 'monospace', fontSize: '14px', marginTop: '3px', fontWeight: 700 }}>
                    646180157088992112
                  </div>
                  <div style={{ fontSize: '12px', color: '#7d5411', marginTop: '4px', fontWeight: 600 }}>
                    STP · Alta reciente (&lt; 15 min)
                  </div>
                </div>

                {/* Paused Intervention Banner */}
                <div
                  style={{
                    backgroundColor: 'rgba(140, 47, 57, 0.08)',
                    border: '1.5px solid #8c2f39',
                    borderRadius: '8px',
                    padding: '16px',
                  }}
                >
                  <div
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px',
                      color: '#8c2f39',
                      fontSize: '12px',
                      fontWeight: 700,
                      letterSpacing: '0.1em',
                      textTransform: 'uppercase',
                      marginBottom: '6px',
                    }}
                  >
                    <span style={{ fontSize: '15px' }}>⚠️</span>
                    <span>Pausa de seguridad</span>
                  </div>
                  <div style={{ fontSize: '13.5px', lineHeight: 1.45, color: '#444141' }}>
                    Detectamos una llamada activa simultánea. Los bancos nunca solicitan transferencias por teléfono.
                  </div>
                </div>

                {/* Protection Outcome CTA Button */}
                <div
                  style={{
                    backgroundColor: '#8c2f39',
                    color: '#ffffff',
                    fontSize: '14px',
                    letterSpacing: '0.06em',
                    textTransform: 'uppercase',
                    padding: '16px',
                    borderRadius: '8px',
                    fontWeight: 700,
                    textAlign: 'center',
                    boxShadow: '0 4px 14px rgba(140, 47, 57, 0.35)',
                  }}
                >
                  ✓ $12,450.00 MXN PROTEGIDOS
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Footer Caption */}
      <footer
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          borderTop: '1px solid rgba(32, 31, 29, 0.14)',
          paddingTop: '18px',
          zIndex: 2,
        }}
      >
        <div style={{ fontSize: '13px', color: 'rgba(32, 31, 29, 0.65)' }}>
          API as a Product · Banco de México (SPEI) · Multi-Factor Corroboration Engine
        </div>
        <div style={{ fontSize: '13px', color: 'rgba(32, 31, 29, 0.65)' }}>
          Dashboard en vivo: <span style={{ color: '#b68235', fontWeight: 600 }}>https://sixsevencitos.tech/</span>
        </div>
      </footer>
    </div>
  );
};
